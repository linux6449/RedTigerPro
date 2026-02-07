import socket
import threading
import struct
import sys
import os

class SimpleSOCKS5Server:
    def __init__(self, host='127.0.0.1', port=1080):
        self.host = host
        self.port = port
        self.server_socket = None
        self.running = False
        
    def handle_client(self, client_socket):
        try:
            version = client_socket.recv(1)
            if version != b'\x05':
                client_socket.close()
                return
                
            nmethods = client_socket.recv(1)[0]
            methods = client_socket.recv(nmethods)
            
            client_socket.send(b'\x05\x00')
            
            request = client_socket.recv(4)
            if request[0] != 0x05 or request[1] != 0x01:
                client_socket.close()
                return
                
            addr_type = request[3]
            
            if addr_type == 0x01:
                address = socket.inet_ntoa(client_socket.recv(4))
            elif addr_type == 0x03:
                domain_length = client_socket.recv(1)[0]
                address = client_socket.recv(domain_length).decode()
            else:
                client_socket.close()
                return
                
            port = struct.unpack('>H', client_socket.recv(2))[0]
            
            try:
                remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                remote_socket.settimeout(10)
                remote_socket.connect((address, port))
                
                bind_addr = socket.inet_aton('0.0.0.0')
                bind_port = struct.pack('>H', self.port)
                client_socket.send(b'\x05\x00\x00\x01' + bind_addr + bind_port)
                
                self.forward_data(client_socket, remote_socket)
                
            except socket.timeout:
                print(f"[!] Timeout: {address}:{port}")
                client_socket.send(b'\x05\x04\x00\x01\x00\x00\x00\x00\x00\x00')
            except ConnectionRefusedError:
                print(f"[!] Connection refused: {address}:{port}")
                client_socket.send(b'\x05\x05\x00\x01\x00\x00\x00\x00\x00\x00')
            except Exception as e:
                print(f"[!] Error: {e}")
                client_socket.send(b'\x05\x01\x00\x01\x00\x00\x00\x00\x00\x00')
                
        except Exception as e:
            print(f"[!] Client handling error: {e}")
        finally:
            try:
                client_socket.close()
            except:
                pass
    
    def forward_data(self, client_socket, remote_socket):
        def forward(src, dst, src_name, dst_name):
            try:
                while self.running:
                    data = src.recv(8192)
                    if not data:
                        break
                    dst.send(data)
            except:
                pass
        
        thread1 = threading.Thread(target=forward, args=(client_socket, remote_socket, "client", "remote"))
        thread2 = threading.Thread(target=forward, args=(remote_socket, client_socket, "remote", "client"))
        
        thread1.start()
        thread2.start()
        
        thread1.join()
        thread2.join()
        
        try:
            remote_socket.close()
        except:
            pass
    
    def start_server(self):
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.settimeout(1)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            
            self.running = True
            print(f"[✓] SOCKS5 server started: {self.host}:{self.port}")
            print(f"[i] Traffic is now being redirected")
            print(f"[i] Set your browser proxy to: 127.0.0.1:{self.port}")
            
            while self.running:
                try:
                    client_socket, addr = self.server_socket.accept()
                    print(f"[+] New connection: {addr[0]}:{addr[1]}")
                    
                    client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
                    client_thread.daemon = True
                    client_thread.start()
                except socket.timeout:
                    continue
                    
        except KeyboardInterrupt:
            print("\n[!] Interrupted by user")
        except Exception as e:
            print(f"[!] Server error: {e}")
        finally:
            self.stop_server()
    
    def stop_server(self):
        self.running = False
        if self.server_socket:
            try:
                self.server_socket.close()
            except:
                pass
        print("[✗] SOCKS5 server stopped")
        print("[i] Traffic routing restored to normal")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    print("=" * 50)
    print("SIMPLE SOCKS5 PROXY SERVER")
    print("=" * 50)
    print("\nWhat does this program do?")
    print("• Starts a proxy server (port: 1080)")
    print("• Redirects traffic for your browser/applications")
    print("• Can be used for: IP masking, bypassing access restrictions")
    print("\nWARNING: No encryption! Do not use for sensitive data!")
    print("\n" + "=" * 50)
    print("SELECT OPTION:")
    print("1 - Turn Proxy Server ON")
    print("2 - Turn Proxy Server OFF")
    print("3 - Exit")
    print("=" * 50)

def main():
    server = SimpleSOCKS5Server('127.0.0.1', 1080)
    server_thread = None
    
    while True:
        clear_screen()
        show_menu()
        
        try:
            choice = input("\nSelect (1-3): ").strip()
            
            if choice == "1":
                if not server.running:
                    print("\n[*] Starting server...")
                    server_thread = threading.Thread(target=server.start_server)
                    server_thread.daemon = True
                    server_thread.start()
                    
                    import time
                    time.sleep(1)
                    
                    if server.running:
                        print("\n[✓] Server started successfully!")
                        print("\n[USAGE GUIDE]")
                        print("1. Browser settings → Proxy/Network settings")
                        print("2. Manual proxy configuration:")
                        print("   - IP: 127.0.0.1")
                        print("   - Port: 1080")
                        print("   - Type: SOCKS5")
                        print("\nPress Enter to continue...")
                        input()
                    else:
                        print("\n[!] Failed to start server!")
                        input("Press Enter to continue...")
                else:
                    print("\n[!] Server is already running!")
                    input("Press Enter to continue...")
                    
            elif choice == "2":
                if server.running:
                    print("\n[*] Stopping server...")
                    server.stop_server()
                    if server_thread:
                        server_thread.join(timeout=2)
                    print("\n[✓] Server stopped!")
                    print("[i] Don't forget to disable proxy settings in your browser!")
                    input("\nPress Enter to continue...")
                else:
                    print("\n[!] Server is already stopped!")
                    input("Press Enter to continue...")
                    
            elif choice == "3":
                print("\n[*] Exiting...")
                if server.running:
                    server.stop_server()
                break
                
            else:
                print("\n[!] Invalid selection! Choose 1, 2, or 3!")
                input("Press Enter to continue...")
                
        except KeyboardInterrupt:
            print("\n\n[*] Exiting...")
            if server.running:
                server.stop_server()
            break

if __name__ == "__main__":
    main()
