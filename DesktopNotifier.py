# This is a notification script in Python.First we install win10toast with pip.The code below reads a text
# in txt document saved in my computer, you see the path.You can use the script without the path, but its gonna be
# somehow useless.Your job is to find a way to use this script properly.


from win10toast import ToastNotifier

notifier = ToastNotifier()
document = open("D:\\Programming\\Notify.txt", "r")
notifier.show_toast(document.read(), duration=10)
