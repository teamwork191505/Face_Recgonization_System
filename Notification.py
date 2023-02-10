# # from plyer import notification
# # import time
# #
# # while True:
# #     time.sleep(2)
# #     notification.notify(
# #         title='Alert From Police HQ',
# #         message='Suspected person found in your area',
# #         app_icon="Notif.ico",
# #         timeout=8,
# #     )
# # # cv2.imshow(images/Het.jpg)
# # # cv2.imshow(images/RDJ.jpg)
# # # cv2.waitKey(0)
# from plyer import notification

import webbrowser
from win10toast_click import ToastNotifier

link = "https://github.com/Thursday1509/FRS-Version_1.0"


def open_link():
    try:
        webbrowser.open_new(link)
    except:
        print("Failed due to poor connection")


toast = ToastNotifier
ToastNotifier.show_toast("Alert from police HQ", "click to get details", duration=20, callback_on_click=open_link,
                 icon_path=r'C:\Users\dhiry\PycharmProjects\FRS-New\Recognization code\Notif.ico')
