# Copyright (c) RedTigerpro
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.


try:
    import sys
    import os
    import subprocess
    import time
    import importlib.util

    def check_python_version():
        if sys.version_info < (3, 6):
            print("Error: Python 3.6 or newer required!")
            return False
        print(f"Python version: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
        return True

    def is_package_installed(package_name):
        try:
            importlib.import_module(package_name)
            return True
        except ImportError:
            alternative_names = {
                'PIL': 'PIL',
                'Pillow': 'PIL',
                'pycryptodome': 'Crypto',
                'cryptography': 'cryptography',
                'beautifulsoup4': 'bs4',
                'pyzipper': 'pyzipper',
                'customtkinter': 'customtkinter',
                'discord': 'discord',
                'opencv-python': 'cv2',
                'pyautogui': 'pyautogui',
                'selenium': 'selenium',
                'pywin32': 'win32api',
                'pyqt5': 'PyQt5',
                'pyqtwebengine': 'PyQt5.QtWebEngine',
                'colorama': 'colorama',
                'requests': 'requests'
            }
            
            if package_name in alternative_names:
                try:
                    importlib.import_module(alternative_names[package_name])
                    return True
                except ImportError:
                    return False
            return False

    def install_package(package, max_retries=3):
        for attempt in range(max_retries):
            try:
                print(f"  Installing: {package} (attempt {attempt + 1}/{max_retries})")
                subprocess.check_call(
                    [sys.executable, "-m", "pip", "install", "--upgrade", package],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                
                if is_package_installed(package):
                    print(f"  {package} successfully installed")
                    return True
                else:
                    print(f"  {package} installed but cannot be imported")
                    return False
                    
            except subprocess.CalledProcessError:
                if attempt < max_retries - 1:
                    print(f"  Retrying to install {package}...")
                    time.sleep(2)
                else:
                    print(f"  Failed to install {package} after {max_retries} attempts")
        return False

    def install_requirements():
        requirements_file = "requirements.txt"
        if not os.path.exists(requirements_file):
            print(f"Error: {requirements_file} not found!")
            return False
        
        print("Processing requirements.txt...")
        try:
            with open(requirements_file, 'r', encoding='utf-8') as f:
                packages = [line.strip() for line in f if line.strip() and not line.startswith('#')]
            
            print(f"Installing {len(packages)} packages...\n")
            
            success_count = 0
            failed_packages = []
            already_installed = 0
            
            for i, package in enumerate(packages, 1):
                print(f"[{i}/{len(packages)}] {package}")
                
                if is_package_installed(package):
                    print(f"  Already installed")
                    already_installed += 1
                    success_count += 1
                    continue
                
                if install_package(package):
                    success_count += 1
                else:
                    failed_packages.append(package)
                
                time.sleep(0.5)
            
            print(f"\nSummary:")
            print(f"   Already installed: {already_installed}")
            print(f"   Newly installed: {success_count - already_installed}")
            print(f"   Failed: {len(failed_packages)}")
            
            if failed_packages:
                print(f"\nFailed packages: {', '.join(failed_packages)}")
                print("Try installing them manually:")
                for pkg in failed_packages:
                    print(f"   pip install {pkg}")
            
            return len(failed_packages) == 0
            
        except Exception as e:
            print(f"Error processing requirements.txt: {e}")
            return False

    def verify_critical_packages():
        critical_packages = ['colorama', 'requests', 'pyzipper']
        missing = []
        
        print("\nChecking critical packages...")
        for package in critical_packages:
            if is_package_installed(package):
                print(f"  ✓ {package}")
            else:
                print(f"  ✗ {package}")
                missing.append(package)
        
        return missing

    def install_basic_packages():
        """Külön telepíti a colorama és requests csomagokat"""
        print("\nInstalling basic required packages...")
        basic_packages = ['colorama', 'requests']
        
        for package in basic_packages:
            if not is_package_installed(package):
                print(f"  Installing {package}...")
                install_package(package)
            else:
                print(f"  ✓ {package} already installed")

    def OpenSites():
        try:
            import webbrowser
            try:
                from Program.Config.Config import telegram, gunslol
            except ImportError:
                pass
            
            print("\nOpening websites...")
            webbrowser.open('https://www.tiktok.com/@anonymus12.1?is_from_webapp=1&sender_device=pc')
            webbrowser.open('https://guns.lol/anonymus12.1')
            print("Websites opened")
        except Exception as e:
            print(f"Failed to open websites: {e}")

    def check_admin_rights():
        if sys.platform.startswith("win"):
            try:
                import ctypes
                return ctypes.windll.shell32.IsUserAnAdmin()
            except:
                return False
        return True

    def main():
        if not check_python_version():
            input("\nPress Enter to exit...")
            return

        if sys.platform.startswith("win"):
            os.system("cls")
            print("="*70)
            print("RedTigerPro Tool Installer - Windows")
            print("="*70)
            
            if check_admin_rights():
                print("✓ Administrator privileges OK")
            else:
                print("⚠ Not running as administrator")
                print("Some packages may require admin privileges.\n")
            
            print("\nInstalling Python modules:\n")
            
            print("Updating pip...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
            
            install_basic_packages()
            
            print("\nInstalling basic packages...")
            install_package("setuptools")
            install_package("wheel")
            
            print("\nInstalling requirements.txt...")
            install_requirements()
            
            missing_critical = verify_critical_packages()
            
            if missing_critical:
                print(f"\n⚠ Some critical packages missing: {', '.join(missing_critical)}")
                print("Try installing them manually:")
                for pkg in missing_critical:
                    print(f"   pip install {pkg}")
                
                if 'pyzipper' in missing_critical:
                    print("\nTrying to install pyzipper separately...")
                    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pyzipper"])
                    
                    if is_package_installed('pyzipper'):
                        print("✓ pyzipper is now installed")
                        missing_critical.remove('pyzipper')
            
            OpenSites()
            
            print("\n" + "="*70)
            if not missing_critical:
                print("✓ All critical packages installed!")
                
                print("\nStarting RedTigerPro Tool in 3 seconds...")
                time.sleep(3)
                os.system(f'"{sys.executable}" RedTigerPro.py')
            else:
                print(f"✗ Missing critical packages: {', '.join(missing_critical)}")
                print("Please install them manually and try again.")
                input("\nPress Enter to exit...")

        elif sys.platform.startswith("linux"):
            os.system("clear")
            print("="*70)
            print("RedTigerPro Tool Installer - Linux")
            print("="*70)
            
            print("\nInstalling Python modules:\n")
            
            print("Updating pip...")
            os.system("pip3 install --upgrade pip")
            
            install_basic_packages()
            
            print("\nInstalling basic packages...")
            os.system("pip3 install setuptools wheel")
            
            print("\nInstalling requirements.txt...")
            if os.path.exists("requirements.txt"):
                os.system("pip3 install -r requirements.txt")
            else:
                print("requirements.txt not found!")
            
            missing_critical = verify_critical_packages()

            OpenSites()
            
            if not missing_critical:
                print("\nStarting RedTigerPro Tool...")
                time.sleep(2)
                os.system("python3 RedTigerPro.py")
            else:
                print(f"\nMissing critical packages: {', '.join(missing_critical)}")
        
        print("\n" + "="*70)
        print("Installation completed!")
        print("="*70)
    
    main()

except KeyboardInterrupt:
    print("\n\nInstallation interrupted by user.")
    input("\nPress Enter to exit...")

except Exception as e:
    print(f"\nUnexpected error: {e}")
    import traceback
    traceback.print_exc()
    input("\nPress Enter to exit...")