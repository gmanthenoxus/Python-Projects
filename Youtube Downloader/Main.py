from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sys
import datetime
from pytube import YouTube
class MainUi(QMainWindow):
    def __init__(self):
        super(MainUi, self).__init__()

        loadUi("Main.ui", self)
        self.btDownload.clicked.connect(self.DownloadVideo)

# Definition of Download Function
    def DownloadVideo(self):
        url = self.lSearch.text()
        downloadPath = "" #Enter Video Path
        Video = YouTube(url)
        mb = 1024 * 1024 # conversion to mb
        stream = Video.streams.get_highest_resolution()
        videoSize = str('%.2f' % ((stream.filesize)/ mb)) + 'MB'
        videoDate = str(Video.publish_date)
        videoTime = Video.length
        finalTime = str(datetime.timedelta(seconds = videoTime))
        videoName = str(Video.title)
        self.dSize.setText(videoSize)
        self.dDate.setText(videoDate)
        self.dTime.setText(finalTime)
        self.dName.setText(videoName)
        stream.download(output_path = downloadPath)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainUi()
    ui.show()
    app.exec_()
