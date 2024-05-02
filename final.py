# import globalPluginHandler
# import time
# import threading
# from logHandler import log
# import watchdog
# import gc
# import sys
# import ctypes  # This is needed for handling COM errors

# class GlobalPlugin(globalPluginHandler.GlobalPlugin):
#     """
#     An NVDA global plugin to monitor and manage periodic freezes by enhancing the watchdog functionality.
#     """
#     def __init__(self):
#         super(GlobalPlugin, self).__init__()
#         self.lastCheckTime = time.time()
#         self.freezeDetected = False
#         self.freezeCount = 0

#         # Start a background thread to monitor NVDA's responsiveness
#         self.monitorThread = threading.Thread(target=self.monitorNVDA, daemon=True)
#         self.monitorThread.start()
#         log.info("Enhanced watchdog monitoring initialized.")

#     def monitorNVDA(self):
#         """
#         Monitors NVDA's responsiveness and attempts recovery if freezes are detected repeatedly.
#         """
#         while True:
#             time.sleep(0.5)  # Monitor every 500 milliseconds
#             currentCheckTime = time.time()

#             # Try to check watchdog recovery and handle exceptions
#             try:
#                 if watchdog.isAttemptingRecovery:
#                     if not self.freezeDetected:
#                         self.freezeDetected = True
#                         self.freezeCount += 1
#                         log.info(f"Freeze #{self.freezeCount} detected. Starting recovery process.")
#                     self.handleFreeze(currentCheckTime)
#                 else:
#                     self.freezeDetected = False
#             except ctypes.COMError as com_error:
#                 if com_error.hresult == -2147023179:  # Check for the specific COM error
#                     log.info("no errors")  # Log "no errors" if the specific error is caught
#                 else:
#                     log.error(f"Unhandled COM error: {com_error}")
#             finally:
#                 self.lastCheckTime = currentCheckTime

#     def handleFreeze(self, currentCheckTime):
#         """
#         Handles the freeze condition by applying recovery procedures if the freeze state persists.
#         """
#         elapsed_time_since_last_freeze = currentCheckTime - self.lastCheckTime
#         if elapsed_time_since_last_freeze >= 10:  # If the freeze state persists for more than 10 seconds
#             log.warning(f"Freeze #{self.freezeCount} persisted for {elapsed_time_since_last_freeze} seconds. Executing recovery.")
#             self.performRecovery()

#     def performRecovery(self):
#         """
#         Performs recovery actions such as clearing the garbage collector to possibly free up resources.
#         """
#         gc.collect()  # Perform garbage collection
#         log.info("Garbage collection performed. Additional recovery mechanisms can be implemented.")
import globalPluginHandler
import time
import threading
from logHandler import log
import watchdog
import gc
import sys
import ctypes  # This is needed for handling COM errors

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    """
    An NVDA global plugin to monitor and manage periodic freezes by enhancing the watchdog functionality.
    """
    def __init__(self):
        super(GlobalPlugin, self).__init__()
        self.lastCheckTime = time.time()
        self.freezeDetected = False
        self.freezeCount = 0

        # Start a background thread to monitor NVDA's responsiveness
        self.monitorThread = threading.Thread(target=self.monitorNVDA, daemon=True)
        self.monitorThread.start()
        print("Enhanced watchdog monitoring initialized.")

    def monitorNVDA(self):
        """
        Monitors NVDA's responsiveness and attempts recovery if freezes are detected repeatedly.
        """
        while True:
            time.sleep(0.5)  # Monitor every 500 milliseconds
            currentCheckTime = time.time()

            # Try to check watchdog recovery and handle exceptions
            try:
                if watchdog.isAttemptingRecovery:
                    if not self.freezeDetected:
                        self.freezeDetected = True
                        self.freezeCount += 1
                        print(f"Freeze #{self.freezeCount} detected. Starting recovery process.")
                    self.handleFreeze(currentCheckTime)
                else:
                    if self.freezeDetected:
                        print("System recovered from freeze.")
                    self.freezeDetected = False
            except ctypes.COMError as com_error:
                if com_error.hresult == -2147023179:  # Check for the specific COM error
                    print("COM error detected but not problematic.")
                else:
                    print(f"Unhandled COM error: {com_error}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
            finally:
                self.lastCheckTime = currentCheckTime

    def handleFreeze(self, currentCheckTime):
        """
        Handles the freeze condition by applying recovery procedures if the freeze state persists.
        """
        elapsed_time_since_last_freeze = currentCheckTime - self.lastCheckTime
        print(f"Handling freeze condition. Elapsed time since last check: {elapsed_time_since_last_freeze} seconds.")
        if elapsed_time_since_last_freeze >= 10:  # If the freeze state persists for more than 10 seconds
            print(f"Freeze #{self.freezeCount} persisted for {elapsed_time_since_last_freeze} seconds. Executing recovery.")
            self.performRecovery()

    def performRecovery(self):
        """
        Performs recovery actions such as clearing the garbage collector to possibly free up resources.
        """
        gc.collect()  # Perform garbage collection
        print("Garbage collection performed. Additional recovery mechanisms can be implemented.")

# Initialize the global plugin
GlobalPlugin()

