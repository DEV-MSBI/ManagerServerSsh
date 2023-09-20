# -*- coding: utf-8 -*-
from PySide2 import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from decimal import Decimal
import sys
import platform
import psutil
from threading import Thread
import traceback
from main import Ui_MainWindow
from login_2 import Ui_MainWindow1
import os
import time
from os import path
import socket
import paramiko
enable_1 = True
maxWidth_1 = 250
maxWidth = 80
enable = True
#ui,_ = loadUiType(path.join(path.dirname(__file__),"main.ui"))
#ui1,_ = loadUiType(path.join(path.dirname(__file__),"main_2.ui"))
WINDOWS_SIZE = 0
#cpu_percent = 0
command = ""
        
class MainApp(QMainWindow, Ui_MainWindow):
    #def __init__(self , parent=None):
    def __init__(self):
        #super(MainApp , self).__init__(*args, **kwargs)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Buttons()
        self.Handel_ui()
        #self.start_work()     
        self.setWindowFlag(Qt.FramelessWindowHint)
        

        self.timer = QTimer()
        self.timer.setInterval(10000)
        self.timer.timeout.connect(self.start_work)
        self.timer.start()

        
        # ###############################################
        # Function to Move window on mouse drag event on the tittle bar
        # ###############################################
        def moveWindow(e):
            # Detect if the window is  normal size
            # ###############################################  
            if self.isMaximized() == False: #Not maximized
                # Move window only when window is normal size  
                # ###############################################
                #if left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:  
                    #Move window 
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        #######################################################################

        #######################################################################
        # Add click event/Mouse move event/drag event to the top header to move the window
        #######################################################################
        self.frame_2.mouseMoveEvent = moveWindow
        #######################################################################


    def mousePressEvent(self, event):
        # ###############################################
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()
        
        
        # We will use this value to move the window

    def restart_remot_httpd(self):
        self.pushButton_6.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.pushButton_9.setEnabled(False)
        self.pushButton_12.setEnabled(False)
        self.pushButton_11.setEnabled(False)
        self.pushButton_13.setEnabled(False)
        self.pushButton_14.setEnabled(False)
        self.pushButton_15.setEnabled(False)
        self.pushButton_16.setEnabled(False)
        self.pushButton_17.setEnabled(False)
        self.pushButton_18.setEnabled(False)
        
        self.thread10 = SSHThread2()

        self.thread10.updateoutput_1.connect(self.restart_httpd)
        self.thread10.start()
        self.thread10.finished.connect(self.thread10.deleteLater)
             
    def start_remot_httpd(self):
        self.pushButton_17.setText("Chargement en cours...")
        self.pushButton_17.setEnabled(False)
        
        self.pushButton_6.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.pushButton_9.setEnabled(False)
        self.pushButton_12.setEnabled(False)
        self.pushButton_11.setEnabled(False)
        self.pushButton_13.setEnabled(False)
        self.pushButton_14.setEnabled(False)
        self.pushButton_15.setEnabled(False)
        self.pushButton_16.setEnabled(False)
        self.pushButton_10.setEnabled(False)
        self.pushButton_18.setEnabled(False)
        self.thread11 = SSHThread3()

        self.thread11.updateoutput_2.connect(self.start_httpd)
        self.thread11.start()
        self.thread11.finished.connect(self.thread11.deleteLater)

    def stop_remot_httpd(self):
        self.pushButton_6.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.pushButton_9.setEnabled(False)
        self.pushButton_12.setEnabled(False)
        self.pushButton_11.setEnabled(False)
        self.pushButton_13.setEnabled(False)
        self.pushButton_14.setEnabled(False)
        self.pushButton_15.setEnabled(False)
        self.pushButton_16.setEnabled(False)
        self.pushButton_10.setEnabled(False)
        self.pushButton_17.setEnabled(False)
        self.thread12 = SSHThread1()
        self.thread12.updateoutput_3.connect(self.stop_httpd)
        self.thread12.start()
        self.thread12.finished.connect(self.thread12.deleteLater)

    def restart_remot_pmta(self):
        self.pushButton_6.setEnabled(False)
        self.pushButton_10.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.pushButton_9.setEnabled(False)
        self.pushButton_12.setEnabled(False)
        self.pushButton_11.setEnabled(False)
        self.pushButton_13.setEnabled(False)
        self.pushButton_14.setEnabled(False)
        self.pushButton_15.setEnabled(False)
        self.pushButton_16.setEnabled(False)
        self.pushButton_17.setEnabled(False)
        self.pushButton_18.setEnabled(False)
        self.thread13 = SSHThread4()
        self.thread13.updateoutput_4.connect(self.restart_pmta)
        self.thread13.start()
        self.thread13.finished.connect(self.thread13.deleteLater)

    def start_remot_pmta(self):
        self.pushButton_6.setEnabled(False)
        self.pushButton_10.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.pushButton_9.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_11.setEnabled(False)
        self.pushButton_13.setEnabled(False)
        self.pushButton_14.setEnabled(False)
        self.pushButton_15.setEnabled(False)
        self.pushButton_16.setEnabled(False)
        self.pushButton_17.setEnabled(False)
        self.pushButton_18.setEnabled(False)
        self.thread14 = SSHThread5()
        self.thread14.updateoutput_5.connect(self.start_pmta)
        self.thread14.start()
        self.thread14.finished.connect(self.thread14.deleteLater)

    def stop_remot_pmta(self):
        self.pushButton_6.setEnabled(False)
        self.pushButton_10.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.pushButton_9.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_12.setEnabled(False)
        self.pushButton_13.setEnabled(False)
        self.pushButton_14.setEnabled(False)
        self.pushButton_15.setEnabled(False)
        self.pushButton_16.setEnabled(False)
        self.pushButton_17.setEnabled(False)
        self.pushButton_18.setEnabled(False)
        self.thread15 = SSHThread6()
        self.thread15.updateoutput_6.connect(self.stop_pmta)
        self.thread15.start()
        self.thread15.finished.connect(self.thread15.deleteLater)

    def Show_journal_logs(self):
        self.pushButton_19.setText("Chargement en cours...")
        self.pushButton_19.setEnabled(False)
        self.thread17 = SSHThread7()
        self.thread17.updateoutput_8.connect(self.show_jrnl)
        self.thread17.start()
        self.thread17.finished.connect(self.thread17.deleteLater)

    def Show_ssh_logs(self):
        self.Show_ssh_log.setText("Chargement en cours...")
        self.Show_ssh_log.setEnabled(False)
        self.thread18 = SSHThread8()
        self.thread18.updateoutput_9.connect(self.show_sshlogs)
        self.thread18.start()
        self.thread18.finished.connect(self.thread18.deleteLater)

    def Show_access_log(self):
        self.Show_acc_log_httpd.setText("Chargement en cours...")
        self.Show_acc_log_httpd.setEnabled(False)
        
        self.thread19 = SSHThread9()
        
        self.thread19.updateoutput_10.connect(self.show_accesslog)
        self.thread19.start()
        self.thread19.finished.connect(self.thread19.deleteLater)

    def Show_error_log(self):
        self.pushButton_24.setText("Chargement en cours...")
        self.pushButton_24.setEnabled(False)
        
        self.thread20 = SSHThread10()
        self.thread20.updateoutput_11.connect(self.show_errorlog)
        self.thread20.start()
        self.thread20.finished.connect(self.thread20.deleteLater)

    def clear_httpd_log(self):
        self.pushButton_26.setText("Chargement en cours...")
        self.pushButton_26.setEnabled(False)
        self.thread21 = SSHThread11()
        self.thread21.updateoutput_12.connect(self.clear_httpdlog)
        self.thread21.start()
        self.thread21.finished.connect(self.thread21.deleteLater)

    def Excute_Cmd1(self):
        global command
        command = self.lineEdit.text()
        self.thread16 = Thread_Excute_Cmd()

        self.thread16.updateoutput_7.connect(self.show_Excute_Cmd)
        self.thread16.start()
        self.thread16.finished.connect(self.thread16.deleteLater)
      
        
    def start_work(self):
        self.thread1 = ProgressThread2()
        self.thread2 = ProgressThread1()
        self.thread6 = ProgressThread3()
        self.thread7 = ProgressThread4()
        self.thread8 = ProgressThread()
        self.thread9 = ProgressThread()
        
        self.thread1.updateProgress.connect(self.updateProgress1)
        self.thread2.updateProgress_1.connect(self.updateProgress2)
        self.thread6.updateProgress_5.connect(self.updateProgress6)
        self.thread7.updateProgress_6.connect(self.updateProgress7)
        self.thread8.updateProgress_7.connect(self.updateProgress8)
        self.thread9.updateProgress_8.connect(self.updateProgress9)
        self.thread1.start()
        self.thread2.start()
        self.thread6.start()
        self.thread7.start()
        self.thread8.start()
        self.thread9.start()
        self.thread1.finished.connect(self.thread1.deleteLater)
        self.thread2.finished.connect(self.thread2.deleteLater)
        self.thread6.finished.connect(self.thread6.deleteLater)
        self.thread7.finished.connect(self.thread7.deleteLater)
        self.thread8.finished.connect(self.thread8.deleteLater)
        self.thread9.finished.connect(self.thread9.deleteLater)
        

    def updateProgress1(self, value):
        self.ProgressBar.rpb_setValue(value)

    def updateProgress2(self, value):
        self.ProgressBar1.rpb_setValue(value)

    def updateProgress6(self, value):
        self.ProgressBar2.rpb_setValue(value)

    def updateProgress7(self, value):
        self.widget_15.rpb_setValue(value)

    def updateProgress8(self, value):
        self.sent_label.setText('Sent: {:.2f} kbps'.format(value))
        self.progressBar_1.setValue(value)
        #pass
 
    def updateProgress9(self, value):
        self.recv_label.setText('Received: {:.2f} kbps'.format(value))
        self.progressBar_2.setValue(value)
        #pass
    
        
    def closeEvent(self, event):
        """self.thread1.quit()
        self.thread2.quit()
        self.thread6.quit()
        self.thread7.quit()
        self.thread8.quit()
        self.thread9.quit()
        self.thread10.quit()"""
        self.thread1.requestInterruption()
        self.thread1.wait()
        self.thread2.requestInterruption()
        self.thread2.wait()
        self.thread6.requestInterruption()
        self.thread6.wait()
        self.thread7.requestInterruption()
        self.thread7.wait()
        self.thread8.requestInterruption()
        self.thread8.wait()
        self.thread9.requestInterruption()
        self.thread9.wait()
        self.thread10.requestInterruption()
        self.thread10.wait()
        self.thread11.requestInterruption()
        self.thread11.wait()
        self.thread12.requestInterruption()
        self.thread12.wait()
        self.thread13.requestInterruption()
        self.thread13.wait()
        self.thread14.requestInterruption()
        self.thread14.wait()
        self.thread15.requestInterruption()
        self.thread15.wait()
        self.thread16.requestInterruption()
        self.thread16.wait()
        self.thread17.requestInterruption()
        self.thread17.wait()
        self.thread18.requestInterruption()
        self.thread18.wait()
        self.thread19.requestInterruption()
        self.thread19.wait()
        self.thread20.requestInterruption()
        self.thread20.wait()
        self.thread21.requestInterruption()
        self.thread21.wait()
        event.accept()
        
            
    def Handel_ui(self):
        global client
        
        self.setWindowTitle('LOGIN')
        #self.setFixedSize(397,396)
        #self.ProgressBar.rpb_setMaximum(900)
        #SETTING THE STYLE OF THE ROUND PROGRESS BAR:
        self.ProgressBar.rpb_setCircleRatio(0.9) #SEE BELOW FOR INFO ON CIRCLE
        self.ProgressBar.rpb_setBarStyle('Pizza')
        self.ProgressBar.rpb_setCircleColor((255, 255, 255))
        #self.ProgressBar.rpb_setCircleColor((194, 222, 236))
        self.ProgressBar.rpb_setLineColor((46, 230, 230))
        
        self.ProgressBar.rpb_setLineWidth(10)
        self.ProgressBar.rpb_setMinimumSize(150, 150)

        self.ProgressBar1.rpb_setCircleRatio(0.9) #SEE BELOW FOR INFO ON CIRCLE
        self.ProgressBar1.rpb_setBarStyle('Pizza')
        self.ProgressBar1.rpb_setCircleColor((255, 255, 255))
        self.ProgressBar1.rpb_setLineColor((46, 230, 230))
        
        self.ProgressBar1.rpb_setLineWidth(10)
        self.ProgressBar1.rpb_setMinimumSize(150, 150)

        self.ProgressBar2.rpb_setCircleRatio(0.8) #SEE BELOW FOR INFO ON CIRCLE
        self.ProgressBar2.rpb_setBarStyle('Pizza')
        self.ProgressBar2.rpb_setCircleColor((255, 255, 255))
        self.ProgressBar2.rpb_setLineColor((255, 170, 0))
        
        self.ProgressBar2.rpb_setLineWidth(8)
        self.ProgressBar2.rpb_setMinimumSize(100, 100)

        self.widget_15.rpb_setCircleRatio(0.8) #SEE BELOW FOR INFO ON CIRCLE
        self.widget_15.rpb_setBarStyle('Pizza')
        self.widget_15.rpb_setCircleColor((255, 255, 255))
        self.widget_15.rpb_setLineColor((255, 170, 0))
        
        self.widget_15.rpb_setLineWidth(8)
        self.widget_15.rpb_setMinimumSize(100, 100)


        '''self.ProgressBar1.spb_setValue((58, 65, 25))
        self.ProgressBar1.spb_setMinimumSize(150, 150)
        self.ProgressBar1.spb_lineColor(((24, 102, 142), (31, 129, 196), (89, 193, 211)))
        self.ProgressBar1.spb_pathColor(((194, 222, 236), (194, 222, 236), (194, 222, 236)))
        
        '''

        '''client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect("83.171.249.214", "22", username="root", password="hwH4HVwnUTUvqa4M")
        '''
        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(Host, Port, username=Username, password=Password)
        
        stdin_4, stdout_4, stderr_4 = client.exec_command("lscpu | grep 'CPU MHz'")
        output_4 = stdout_4.read().decode("utf-8").strip()
        cpu_info1 = output_4
        self.label_5.setText(str(cpu_info1))

        stdin_2, stdout_2, stderr_2 = client.exec_command("""echo "import psutil
mem = psutil.virtual_memory()
print('RAM size: {:.2f} GB'.format(mem.total/1024/1024/1024))" > ram_s.py | python3 ram_s.py""")
        output_2 = stdout_2.read().decode("utf-8").strip()
        ram_size = output_2
        self.label_4.setText(str(ram_size))
        
        stdin_8, stdout_8, stderr_8 = client.exec_command("lsblk -b /dev/sda")
        #stdin_8, stdout_8, stderr_8 = client.exec_command("lsblk -b /dev/xvda")
        #stdin_8, stdout_8, stderr_8 = client.exec_command("lsblk -b /dev/vda")
        output_8 = stdout_8.read().decode("utf-8").strip()
        
        size = int(output_8.split()[10])
        
        size_gb = size / (1024 ** 3)
        self.label_8.setText("HD Size: {:.2f} GB".format(size_gb))

        stdin_9, stdout_9, stderr_9 = client.exec_command("""echo "import psutil
usage = psutil.disk_usage('/')
available_space = usage.free / (1024.0 ** 3)
print(str(available_space))" > usage_free.py | python3 usage_free.py""")
        output_9 = stdout_9.read().decode("utf-8").strip()

        self.label_9.setText("HD Available Space: {:.2f} GB".format(float(output_9)))

        stdin_10, stdout_10, stderr_10 = client.exec_command("""echo "import psutil
usage = psutil.disk_usage('/')
available_space = usage.used / (1024.0 ** 3)
print(str(available_space))" > usage_used.py | python3 usage_used.py""")
        output_10 = stdout_10.read().decode("utf-8").strip()

        self.label_10.setText("HD Used Space: {:.2f} GB".format(float(output_10)))
        
    def Handel_Buttons(self):
        
        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.pushButton_4.clicked.connect(self.toggleMenu)

        ## PAGES
        ########################################################################

        # PAGE 1
        self.Home.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Home1))
        
    
        # PAGE 2
        self.Dashboard.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Dashboard1))

        # PAGE 3
        self.Mangsrv.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Mangsrv_1))

        # PAGE 4
        self.event_log.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.log))

        #self.Dashboard.clicked.connect(self.oh_no)
        self.pushButton_10.clicked.connect(self.restart_remot_httpd)
        self.pushButton_11.clicked.connect(self.stop_remot_pmta)
        self.pushButton_7.clicked.connect(self.restart_remot_pmta)
        self.pushButton_12.clicked.connect(self.start_remot_pmta)
        self.pushButton_17.clicked.connect(self.start_remot_httpd)
        self.pushButton_18.clicked.connect(self.stop_remot_httpd)
        self.pushButton_19.clicked.connect(self.Show_journal_logs)
        self.Show_ssh_log.clicked.connect(self.Show_ssh_logs)
        self.Show_acc_log_httpd.clicked.connect(self.Show_access_log)
        self.pushButton_24.clicked.connect(self.Show_error_log)
        self.pushButton_26.clicked.connect(self.clear_httpd_log)
        self.ExcuteCmd.clicked.connect(self.Excute_Cmd1)
        
        self.clear.clicked.connect(self.clear_1)
        self.clear.setEnabled(False)
        self.Clear_2.clicked.connect(self.clear_2)
        self.Clear_2.setEnabled(False)
        self.pushButton_25.clicked.connect(self.clear_3)
        self.pushButton_25.setEnabled(False)
        
        # BTN_Close
        self.Bn_Close.clicked.connect(lambda: self.close())
        # BTN_Minimized
        self.Bn_Min.clicked.connect(lambda: self.showMinimized())
        #BTN_Maxmized
        #self.Bn_Max.clicked.connect(lambda: self.showMaximized())
        self.Bn_Max.clicked.connect(lambda: self.restore_or_max_windows())
        
        time.sleep(2)


    def show_Excute_Cmd(self, value):
        self.output_cmd.setPlainText(value)
        self.Clear_2.setEnabled(True)
        
    def restart_httpd(self, value):
        self.Output.setText(value)
        self.clear.setEnabled(True)

    def start_httpd(self, value):
        self.pushButton_17.setText("  HTTP")
        self.pushButton_17.setEnabled(True)
        self.Output.setText(value)
        self.clear.setEnabled(True)
        
    def stop_httpd(self, value):
        self.Output.setText(value)
        self.clear.setEnabled(True)
  
    def restart_pmta(self, value):
        self.Output.setText(value)
        self.clear.setEnabled(True)
        
    def start_pmta(self, value):
        self.Output.setText(value)
        self.clear.setEnabled(True)
        
    def stop_pmta(self, value):
        self.Output.setText(value)
        self.clear.setEnabled(True)

    def show_jrnl(self, value):
        self.pushButton_19.setText("Show journal logs")
        self.pushButton_19.setEnabled(True)
        self.plainTextEdit.setPlainText(value)
        self.pushButton_25.setEnabled(True)

    def show_sshlogs(self, value):
        self.Show_ssh_log.setText("Show ssh log")
        self.Show_ssh_log.setEnabled(True)
        self.plainTextEdit.setPlainText(value)
        self.pushButton_25.setEnabled(True)

    def show_accesslog(self, value):
        self.Show_acc_log_httpd.setText("Show access log httpd")
        self.Show_acc_log_httpd.setEnabled(True)
        self.plainTextEdit.setPlainText(value)
        self.pushButton_25.setEnabled(True)
            
    def show_errorlog(self, value):
        self.pushButton_24.setText("Show error log httpd")
        self.pushButton_24.setEnabled(True)
        self.plainTextEdit.setPlainText(value)
        self.pushButton_25.setEnabled(True)

    def clear_httpdlog(self, value):
        self.pushButton_26.setText("Clear log httpd")
        self.pushButton_26.setEnabled(True)
        self.plainTextEdit.setPlainText(value)
        self.pushButton_25.setEnabled(True)

    def clear_1(self):
        self.Output.setText("")
        self.clear.setEnabled(False)
        self.pushButton_6.setEnabled(True)
        self.pushButton_7.setEnabled(True)
        self.pushButton_8.setEnabled(True)
        self.pushButton_9.setEnabled(True)
        self.pushButton_10.setEnabled(True)
        self.pushButton_12.setEnabled(True)
        self.pushButton_11.setEnabled(True)
        self.pushButton_13.setEnabled(True)
        self.pushButton_14.setEnabled(True)
        self.pushButton_15.setEnabled(True)
        self.pushButton_16.setEnabled(True)
        self.pushButton_17.setEnabled(True)
        self.pushButton_18.setEnabled(True)

    def clear_2(self):
        self.lineEdit.setText("")
        self.output_cmd.setPlainText("")
        self.Clear_2.setEnabled(False)

    def clear_3(self):
        self.plainTextEdit.setPlainText("")
        self.pushButton_25.setEnabled(False)

    def restore_or_max_windows(self):
        global WINDOWS_SIZE
        win_status = WINDOWS_SIZE
        if win_status == 0:
            self.showMaximized()
            WINDOWS_SIZE = 1
            self.Bn_Max.setIcon(QIcon("icon/restore.png"))
        else:
            WINDOWS_SIZE = 0
            self.showNormal() 
            self.Bn_Max.setIcon(QIcon("icon/1949135.png"))
    
    def toggleMenu(self):
        if enable:

            # GET WIDTH
            width = self.left_menu1.width()
            maxExtend = maxWidth
            standard = 0

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.left_menu1 , b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
            
#Thread Excute command
class Thread_Excute_Cmd(QThread):
    updateoutput_7 = Signal(str)
    def run(self):
        stdin_cmd, stdout_cmd, stderr_cmd = client.exec_command(command)
        output_cmd = stdout_cmd.read().decode("utf-8").strip()
        output_err_cmd = stderr_cmd.read().decode("utf-8").strip()
                
        if output_err_cmd:
            self.updateoutput_7.emit(output_err_cmd)

        else:
            self.updateoutput_7.emit(output_cmd)


class SSHThread1(QThread):
    updateoutput_3 = Signal(str)

    def run(self):

        #stop httpd
        stdin_stp, stdout_stp, stderr_stp = client.exec_command("service httpd stop")
            
        output_stp = stdout_stp.read().decode("utf-8").strip()
        output_err_stp = stderr_stp.read().decode("utf-8").strip()
            
        if output_err_stp:
            self.updateoutput_3.emit(str(output_err_stp))

        else:
            self.updateoutput_3.emit(str(output_stp))
        self.sleep(2)
            
class SSHThread2(QThread):
    updateoutput_1 = Signal(str)

    def run(self):
            
        #restart httpd
        stdin_rs, stdout_rs, stderr_rs = client.exec_command("systemctl restart httpd")  
        output_rs = stdout_rs.read().decode("utf-8").strip()
        output_err = stderr_rs.read().decode("utf-8").strip()
            
        if output_err:
            self.updateoutput_1.emit(str(output_err))

        else:
            self.updateoutput_1.emit("restart (ok)")
            #self.updateoutput_1.emit(str(output_rs))
        self.sleep(2)

class SSHThread3(QThread):
    updateoutput_2 = Signal(str)

    def run(self):
        #start httpd
        stdin_sh, stdout_sh, stderr_sh = client.exec_command("service httpd start")
            
        output_sh = stdout_sh.read().decode("utf-8").strip()
        output_err_sh = stderr_sh.read().decode("utf-8").strip()
            
        if output_err_sh:
            self.updateoutput_2.emit(str(output_err_sh))

        else:
            self.updateoutput_2.emit(str(output_sh))
        self.sleep(2)

#restart pmta
class SSHThread4(QThread):
    updateoutput_4 = Signal(str)
    
    def run(self):
        stdin_pmta, stdout_pmta, stderr_pmta = client.exec_command("service pmta restart")
            
        output_rs1 = stdout_pmta.read().decode("utf-8").strip()
        output_err1 = stderr_pmta.read().decode("utf-8").strip()
           
        if output_err1:
            self.updateoutput_4.emit(str(output_err1))
        else:
            self.updateoutput_4.emit(str(output_rs1))
        self.sleep(2)

#start pmta
class SSHThread5(QThread):
    updateoutput_5 = Signal(str)

    def run(self):
        stdin_spmta, stdout_spmta, stderr_spmta = client.exec_command("service pmta start")
            
        output_rs2 = stdout_spmta.read().decode("utf-8").strip()
        output_err2 = stderr_spmta.read().decode("utf-8").strip()
            
        if output_err2:
            self.updateoutput_5.emit(str(output_err2))
        else:
            self.updateoutput_5.emit(str(output_rs2))
        self.sleep(2)

#stop pmta
class SSHThread6(QThread):
    updateoutput_6 = Signal(str)

    def run(self):
        stdin_stpmta, stdout_stpmta, stderr_stpmta = client.exec_command("service pmta stop")
            
        output_stpmta = stdout_stpmta.read().decode("utf-8").strip()
        output_err2_stpmta = stderr_stpmta.read().decode("utf-8").strip()
            
        if output_err2_stpmta:
            self.updateoutput_6.emit(str(output_err2_stpmta))
        else:
            self.updateoutput_6.emit(str(output_stpmta))
        self.sleep(2)

class SSHThread7(QThread):
    updateoutput_8 = Signal(str)

    def run(self):
        stdin_jrn, stdout_jrn, stderr_jrn = client.exec_command("journalctl")
            
        output_jrn = stdout_jrn.read().decode("utf-8").strip()
        output_err2_jrn = stderr_jrn.read().decode("utf-8").strip()
            
        if output_err2_jrn:
            self.updateoutput_8.emit(str(output_err2_jrn))
        else:
            self.updateoutput_8.emit(str(output_jrn))
        self.sleep(2)

class SSHThread8(QThread):
    updateoutput_9 = Signal(str)

    def run(self):
        stdin_lgssh, stdout_lgssh, stderr_lgssh = client.exec_command("cat /var/log/secure")
            
        output_lgssh = stdout_lgssh.read().decode("utf-8").strip()
        output_err2_lgssh = stderr_lgssh.read().decode("utf-8").strip()
            
        if output_err2_lgssh:
            self.updateoutput_9.emit(str(output_err2_lgssh))
        else:
            self.updateoutput_9.emit(str(output_lgssh))
        self.sleep(1)

class SSHThread9(QThread):
    updateoutput_10 = Signal(str)
   

    def run(self):

        stdin_accesshttpd, stdout_accesshttpd, stderr_accesshttpd = client.exec_command("cat /var/log/httpd/access_log")
            
        output_accesshttpd = stdout_accesshttpd.read().decode("utf-8").strip()
        output_err2_accesshttpd = stderr_accesshttpd.read().decode("utf-8").strip()
            
        if output_err2_accesshttpd:
            self.updateoutput_10.emit(str(output_err2_accesshttpd))
          
        else:
            self.updateoutput_10.emit(str(output_accesshttpd))
           
        
        self.sleep(1)

class SSHThread10(QThread):
    updateoutput_11 = Signal(str)

    def run(self):
        stdin_errorlog, stdout_errorlog, stderr_errorlog = client.exec_command("cat /var/log/httpd/error_log")
            
        output_errorlog = stdout_errorlog.read().decode("utf-8").strip()
        output_err2_errorlog = stderr_errorlog.read().decode("utf-8").strip()
            
        if output_err2_errorlog:
            self.updateoutput_11.emit(str(output_err2_errorlog))
        else:
            self.updateoutput_11.emit(str(output_errorlog))
        self.sleep(1)

class SSHThread11(QThread):
    updateoutput_12 = Signal(str)

    def run(self):
        stdin_clearlog, stdout_clearlog, stderr_clearlog = client.exec_command("""rm -rf /var/log/httpd/error_log-*
rm -rf /var/log/httpd/access_log-*
""")
            
        #output_clearlog = stdout_clearlog.read().decode("utf-8").strip()
        output_err2_clearlog = stderr_clearlog.read().decode("utf-8").strip()
            
        if output_err2_clearlog:
            self.updateoutput_12.emit(str(output_err2_clearlog))
        else:
            self.updateoutput_12.emit(str("Clear log httpd : Ok"))
        self.sleep(1)
        
class ProgressThread1(QThread):
    updateProgress_1 = Signal(float)
    def run(self):
            # run the `free` command to get the memory usage information
            stdin_1, stdout_1, stderr_1 = client.exec_command('free -m')
            memory_info = stdout_1.read().decode('utf-8')

            # extract the memory usage information from the output of the `free` command
            memory_lines = memory_info.strip().split('\n')
            memory_line = memory_lines[1].strip().split()
            total_memory = int(memory_line[1])
            used_memory = int(memory_line[2])
            free_memory = int(memory_line[3])

            # calculate the percentage of used memory
            memory_usage = (used_memory / total_memory) * 100
            self.updateProgress_1.emit(memory_usage)

class ProgressThread2(QThread):
    updateProgress = Signal(float)
    def run(self): 
        stdin, stdout, stderr = client.exec_command("top -bn1 | grep 'Cpu(s)' | sed 's/.*, *\\([0-9.]*\\)%* id.*/\\1/' | awk '{print 100 - $1}'")
        output = stdout.read().decode("utf-8").strip()
        cpu_percent = output

        self.updateProgress.emit(float(cpu_percent))
        
class ProgressThread3(QThread):
    updateProgress_5 = Signal(int)
    def run(self):
        #activity hard drive
        stdin_5, stdout_5, stderr_5 = client.exec_command("iostat -d -x -k -t /dev/sda")
        #stdin_5, stdout_5, stderr_5 = client.exec_command("iostat -d -x -k -t /dev/xvda")
        #stdin_5, stdout_5, stderr_5 = client.exec_command("iostat -d -x -k -t /dev/vda")
        output_5 = stdout_5.read().decode("utf-8").strip()
            
        activity = output_5.split("\n")[-1].split()[-1]
        self.updateProgress_5.emit(float(activity))

class ProgressThread4(QThread):
    updateProgress_6 = Signal(int)
    def run(self):
        #usage hard drive
        stdin_6, stdout_6, stderr_6 = client.exec_command("df / | tail -1")
        output_6 = stdout_6.read().decode("utf-8").strip()
        usage = int(output_6.split()[4][:-1])
        self.updateProgress_6.emit(float(usage))
                     
class ProgressThread(QThread):
    
    updateProgress_7 = Signal(float)
    updateProgress_8 = Signal(float)

    
    def run(self):

        try:  
            stdin_s, stdout_s, stderr_s = client.exec_command("""echo "import psutil
last_sent = psutil.net_io_counters().bytes_sent
net_io_counters = psutil.net_io_counters()
sent_bytes = (net_io_counters.bytes_sent - last_sent) / 1024
sent_kbps = sent_bytes * 8
print(sent_kbps)
last_sent = net_io_counters.bytes_sent" > sent_kbps.py | python3 sent_kbps.py""")
            Sent = stdout_s.read().decode("utf-8").strip()
            
            
            stdin_r, stdout_r, stderr_r = client.exec_command("""echo "import psutil
last_recv = psutil.net_io_counters().bytes_recv
net_io_counters = psutil.net_io_counters()
recv_bytes = (net_io_counters.bytes_recv - last_recv) / 1024
recv_kbps = recv_bytes * 8
print(recv_kbps)
last_recv = net_io_counters.bytes_recv" > recv_kbps.py | python3 recv_kbps.py""")
            Received = stdout_r.read().decode("utf-8").strip()
            
            try:
                float_num = float(Sent)
                float_2 = float(Received)
            except ValueError:
                print("Error: Could not convert string to float.")
            else:
                self.updateProgress_7.emit(float_num)
                self.updateProgress_8.emit(float_2)

            self.sleep(2)
        
            if self.isInterruptionRequested():
                print("Thread interrupted")
            else:
                pass
        except paramiko.ssh_exception.ChannelException as e:
            print("Error: {}".format(e))

class SSHConnectionThread(QThread):
    error_signal = Signal(str)
    success_signal = Signal(str)

    def __init__(self, Host, Port, Username, Password):
        super().__init__()
        self.Host = Host
        self.Username = Username
        self.Password = Password
        self.Port = Port

    def run(self):
        
        "Login to the remote server"
        try:
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(self.Host, self.Port, username=self.Username, password=self.Password)

            connect_ssh = 'connect'

            self.success_signal.emit(connect_ssh)
            
        except Exception as e:
            self.error_signal.emit(str(e))

class MainLogin(QMainWindow , Ui_MainWindow1):
    #def __init__(self , parent=None):
    def __init__(self):
        #super(MainLogin , self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Buttons()
        self.Handel_ui()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # ###############################################
        # Function to Move window on mouse drag event on the tittle bar
        # ###############################################
        def moveWindow(e):
            # Detect if the window is  normal size
            # ###############################################  
            if self.isMaximized() == False: #Not maximized
                # Move window only when window is normal size  
                # ###############################################
                #if left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:  
                    #Move window 
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        #######################################################################

        #######################################################################
        # Add click event/Mouse move event/drag event to the top header to move the window
        #######################################################################
        self.frame.mouseMoveEvent = moveWindow
        #######################################################################


    def mousePressEvent(self, event):
        # ###############################################
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()
        
    def Handel_ui(self):
    
        self.setWindowTitle('LOGIN')
        #self.setFixedSize(397,396)
              
    def Handel_Buttons(self):
        self.opn_login.clicked.connect(self.toggleMenu1)
        self.login.clicked.connect(self.Login)
        # BTN_Close
        self.close_1.clicked.connect(lambda: self.close())
        # BTN_Minimized
        self.min.clicked.connect(lambda: self.showMinimized())
        

    def toggleMenu1(self):
        if enable_1:

            # GET WIDTH
            width_1 = self.frame_3.width()
            maxExtend_1 = maxWidth_1
            standard_1 = 0

            # SET MAX WIDTH
            if width_1 == 0:
                self.opn_login.setText("Close Login")
                widthExtended_1 = maxExtend_1
            else:
                self.opn_login.setText("Open Login")
                widthExtended_1 = standard_1

            # ANIMATION
            self.animation = QPropertyAnimation(self.frame_3 , b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width_1)
            self.animation.setEndValue(widthExtended_1)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
            
    def Login(self):
        
        global Host,Port,Username,Password
        Host = self.Host.text()
        Port = self.Port.text()
        Username = self.Username.text()
        Password = self.Password.text()
        
        self.login.setText("Loading...")
        self.login.setEnabled(False)

        if not Host or not Username or not Password:
            QMessageBox.warning(self, 'Warning', 'Please fill all fields')
            return

        self.ssh_connection_thread = SSHConnectionThread(Host, Port, Username, Password)
        self.ssh_connection_thread.success_signal.connect(self.handle_success)
        #self.ssh_connection_thread.error_signal.connect(self.handle_error)
        self.ssh_connection_thread.start()
        self.ssh_connection_thread.finished.connect(self.ssh_connection_thread.deleteLater)

    def closeEvent(self, event):
        self.ssh_connection_thread.requestInterruption()
        self.ssh_connection_thread.wait()

    def handle_success(self, output):
        print(output)

        self.main = MainApp()
        self.main.show()# SHOW Login
        self.close()
        
    def handle_error(self, error):
        QMessageBox.critical(self, 'Error', error)

        
"""class MainLogin(QMainWindow , Ui_MainWindow1):
    #def __init__(self , parent=None):
    def __init__(self):
        #super(MainLogin , self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Buttons()
        self.Handel_ui()
        self.show()
        
        
    def Handel_ui(self):
    
        self.setWindowTitle('LOGIN')
        self.setFixedSize(397,396)
              
    def Handel_Buttons(self):
        self.pushButton.clicked.connect(self.Login)
    
    def Login(self):
        
        global Host,Port,Username,Password
        Host = self.lineEdit.text()
        Port = self.lineEdit_2.text()
        Username = self.lineEdit_3.text()
        Password = self.lineEdit_4.text()
        
        self.pushButton.setText("Chargement ...")
        self.pushButton.setEnabled(False)

        if not Host or not Username or not Password:
            QMessageBox.warning(self, 'Warning', 'Please fill all fields')
            return

        self.ssh_connection_thread = SSHConnectionThread(Host, Port, Username, Password)
        self.ssh_connection_thread.success_signal.connect(self.handle_success)
        #self.ssh_connection_thread.error_signal.connect(self.handle_error)
        self.ssh_connection_thread.start()
        self.ssh_connection_thread.finished.connect(self.ssh_connection_thread.deleteLater)

    def closeEvent(self, event):
        self.ssh_connection_thread.requestInterruption()
        self.ssh_connection_thread.wait()

    def handle_success(self, output):
        print(output)

        self.main = MainApp()
        self.main.show()# SHOW Login
        self.close()
        
    def handle_error(self, error):
        QMessageBox.critical(self, 'Error', error)"""
        


def main():
    app = QApplication(sys.argv)
    window = MainLogin()
    #window = MainApp()
    window.show()
    app.exec_()
    


if __name__ == '__main__':
    main()
