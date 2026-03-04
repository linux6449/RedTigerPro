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
                'requests': 'requests',
                'yt-dlp': 'yt_dlp',
            }
            
            if package_name in alternative_names:
                try:
                    importlib.import_module(alternative_names[package_name])
                    return True
                except ImportError:
                    return False
            return False

    def install_package(package, max_retries=3, pip_cmd=None):
        if pip_cmd is None:
            pip_cmd = [sys.executable, "-m", "pip"]
            
        for attempt in range(max_retries):
            try:
                print(f"  Installing: {package} (attempt {attempt + 1}/{max_retries})")
                result = subprocess.run(
                    pip_cmd + ["install", "--upgrade", package],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                
                if result.returncode == 0 and is_package_installed(package):
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

    def install_requirements(pip_cmd=None):
        if pip_cmd is None:
            pip_cmd = [sys.executable, "-m", "pip"]
            
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
                
                if install_package(package, pip_cmd=pip_cmd):
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
        critical_packages = ['colorama', 'requests', 'pyzipper', 'yt_dlp']
        missing = []
        
        print("\nChecking critical packages...")
        for package in critical_packages:
            if is_package_installed(package):
                print(f"  ✓ {package}")
            else:
                print(f"  ✗ {package}")
                missing.append(package)
        
        return missing

    def install_basic_packages(pip_cmd=None):
        """Külön telepíti a colorama és requests csomagokat"""
        if pip_cmd is None:
            pip_cmd = [sys.executable, "-m", "pip"]
            
        print("\nInstalling basic required packages...")
        basic_packages = ['colorama', 'requests', 'setuptools', 'wheel']
        
        for package in basic_packages:
            if not is_package_installed(package):
                print(f"  Installing {package}...")
                install_package(package, pip_cmd=pip_cmd)
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
        else:
            # Linux-on check if running as root
            return os.geteuid() == 0

    def install_linux_system_packages():
        """Telepíti a szükséges rendszer csomagokat Linuxon"""
        print("\nChecking required system packages...")
        
        system_packages = [
            'python3-pip',
            'python3-dev',
            'python3-venv',
            'build-essential',
            'libssl-dev',
            'libffi-dev',
            'libxml2-dev',
            'libxslt1-dev',
            'zlib1g-dev',
            'ffmpeg'  # yt-dlp-nek ajánlott
        ]
        
        try:
            # Ellenőrizzük, hogy apt-get elérhető-e
            subprocess.run(['which', 'apt-get'], check=True, stdout=subprocess.DEVNULL)
            
            # Frissítjük a csomaglistát
            print("  Updating package list...")
            subprocess.run(['sudo', 'apt-get', 'update'], check=True)
            
            # Telepítjük a csomagokat
            for package in system_packages:
                print(f"  Installing {package}...")
                subprocess.run(
                    ['sudo', 'apt-get', 'install', '-y', package],
                    check=True,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
            
            print("  ✓ System packages installed successfully")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"  ✗ Failed to install system packages: {e}")
            return False
        except FileNotFoundError:
            print("  ✗ apt-get not found. Please install packages manually:")
            print(f"     sudo apt-get install {' '.join(system_packages)}")
            return False

    def main():
        if not check_python_version():
            input("\nPress Enter to exit...")
            return

        if sys.platform.startswith("win"):
            # Windows telepítés
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
            
            pip_cmd = [sys.executable, "-m", "pip"]
            install_basic_packages(pip_cmd)
            install_requirements(pip_cmd)
            
        elif sys.platform.startswith("linux"):
            # Linux telepítés - DENO NÉLKÜL!
            os.system("clear")
            print("="*70)
            print("RedTigerPro Tool Installer - Linux")
            print("="*70)
            
            # Ellenőrizzük a root jogosultságot
            if check_admin_rights():
                print("✓ Root privileges OK")
            else:
                print("⚠ Not running as root!")
                print("Some packages may require root privileges.")
                response = input("Continue anyway? (y/n): ")
                if response.lower() != 'y':
                    sys.exit(1)
            
            # Telepítjük a rendszer csomagokat
            install_linux_system_packages()
            
            print("\nInstalling Python modules:\n")
            
            # Meghatározzuk a pip parancsot
            python_cmd = sys.executable
            pip_cmd = [python_cmd, "-m", "pip"]
            
            # pip frissítés
            print("Updating pip...")
            try:
                subprocess.check_call(pip_cmd + ["install", "--upgrade", "pip"])
                print("  ✓ pip updated successfully")
            except subprocess.CalledProcessError as e:
                print(f"  ✗ Failed to update pip: {e}")
            
            # Alap csomagok telepítése
            install_basic_packages(pip_cmd)
            
            # requirements.txt telepítése
            print("\nInstalling requirements.txt...")
            install_requirements(pip_cmd)
            
            # Ellenőrizzük a kritikus csomagokat
            missing_critical = verify_critical_packages()
            
            # Ha hiányzik a yt-dlp, próbáljuk újra
            if 'yt_dlp' in missing_critical:
                print("\nTrying to install yt-dlp separately...")
                install_package('yt-dlp', pip_cmd=pip_cmd)
                missing_critical = verify_critical_packages()
            
            # Weboldalak megnyitása
            OpenSites()
            
            print("\n" + "="*70)
            
            # Eredmény kiértékelése
            if not missing_critical:
                print("✓ All critical packages installed!")
                print("\nStarting RedTigerPro Tool in 3 seconds...")
                time.sleep(3)
                
                # Indítás
                try:
                    subprocess.run([python_cmd, "RedTigerPro.py"])
                except Exception as e:
                    print(f"Failed to start RedTigerPro.py: {e}")
                    print("You can start it manually with: python3 RedTigerPro.py")
            else:
                print(f"✗ Missing critical packages: {', '.join(missing_critical)}")
                print("\nTrying to install missing packages with pip3...")
                for pkg in missing_critical:
                    pkg_name = pkg.replace('_', '-')  # yt_dlp -> yt-dlp
                    try:
                        subprocess.check_call(['pip3', 'install', '--upgrade', pkg_name])
                        print(f"  ✓ {pkg_name} installed")
                    except:
                        print(f"  ✗ Failed to install {pkg_name}")
                
                print("\nPlease check the errors above and try again.")
                input("\nPress Enter to exit...")
                return
        
        # Közös rész
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