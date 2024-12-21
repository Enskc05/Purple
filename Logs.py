import os
import subprocess
import platform
from datetime import datetime


class LogCollector:
    def __init__(self, log_type="system", duration="1d", log_file="logs.txt"):
        self.log_type = log_type
        self.duration = duration
        self.log_file = log_file
        self.os_platform = platform.system().lower()

    def collect_logs(self):
        with open(self.log_file, 'w') as log_file:
            if self.os_platform == "darwin":
                if self.log_type == "system":
                    self._collect_system_logs_macos(log_file)
                else:
                    self._collect_custom_logs_macos(log_file)
            elif self.os_platform == "windows":
                if self.log_type == "system":
                    self._collect_system_logs_windows(log_file)
                else:
                    self._collect_custom_logs_windows(log_file)
            elif self.os_platform == "linux":
                if self.log_type == "system":
                    self._collect_system_logs_linux(log_file)
                else:
                    self._collect_custom_logs_linux(log_file)
            else:
                log_file.write("Desteklenmeyen bir işletim sistemi.\n")

    def _collect_system_logs_macos(self, log_file):
        command = ["log", "show", "--predicate", "eventMessage contains 'error'", "--info", "--last", self.duration]
        try:
            log_data = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
            log_file.write(f"macOS Sistem logları:\n{log_data}\n")
        except subprocess.CalledProcessError as e:
            log_file.write(f"Komut çalıştırılırken hata oluştu: {e.output}\n")
        except Exception as e:
            log_file.write(f"Beklenmeyen bir hata oluştu: {str(e)}\n")

    def _collect_system_logs_windows(self, log_file):
        command = ["wevtutil", "qe", "System", "/f:Text", "/c:10",
                   "/q:*[System[Provider[@Name='Microsoft-Windows-Windows Defender Antivirus']]]"]
        try:
            log_data = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
            log_file.write(f"Windows Sistem logları:\n{log_data}\n")
        except subprocess.CalledProcessError as e:
            log_file.write(f"Komut çalıştırılırken hata oluştu: {e.output}\n")
        except Exception as e:
            log_file.write(f"Beklenmeyen bir hata oluştu: {str(e)}\n")

    def _collect_system_logs_linux(self, log_file):
        log_files = ["/var/log/syslog", "/var/log/auth.log", "/var/log/kern.log"]
        for log_file_path in log_files:
            if os.path.exists(log_file_path):
                try:
                    with open(log_file_path, 'r') as f:
                        log_file.write(f"Linux logları ({log_file_path}):\n")
                        log_file.write(f.read() + "\n")
                except Exception as e:
                    log_file.write(f"Log dosyasını okurken hata oluştu: {e}\n")
            else:
                log_file.write(f"{log_file_path} dosyası bulunamadı.\n")

    def _collect_custom_logs_macos(self, log_file):
        system_log_path = "/var/log/system.log"
        if os.path.exists(system_log_path):
            try:
                with open(system_log_path, 'r') as system_log:
                    log_file.write(f"macOS System.log dosyasından alınan veriler:\n")
                    log_file.write(system_log.read())
            except Exception as e:
                log_file.write(f"Log dosyasını okurken hata oluştu: {e}\n")
        else:
            log_file.write("macOS'ta system.log dosyası bulunamadı.\n")

    def _collect_custom_logs_windows(self, log_file):
        system_log_path = "C:\\Windows\\System32\\winevt\\Logs\\Application.evtx"
        if os.path.exists(system_log_path):
            try:
                with open(system_log_path, 'r') as system_log:
                    log_file.write(f"Windows Application log dosyasından alınan veriler:\n")
                    log_file.write(system_log.read())
            except Exception as e:
                log_file.write(f"Log dosyasını okurken hata oluştu: {e}\n")
        else:
            log_file.write("Windows'ta Application.evtx dosyası bulunamadı.\n")

    def _collect_custom_logs_linux(self, log_file):
        try:
            log_data = subprocess.check_output(["dmesg"], stderr=subprocess.STDOUT, universal_newlines=True)
            log_file.write(f"Linux dmesg logları:\n{log_data}\n")
        except subprocess.CalledProcessError as e:
            log_file.write(f"Komut çalıştırılırken hata oluştu: {e.output}\n")
        except Exception as e:
            log_file.write(f"Beklenmeyen bir hata oluştu: {str(e)}\n")

    def get_logs(self):
        with open(self.log_file, 'r') as file:
            return file.read()
