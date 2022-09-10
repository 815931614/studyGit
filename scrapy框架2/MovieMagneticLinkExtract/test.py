test = [
"Epic.Adventures.with.Bertie.Gregory.S01.2160p.DSNP.WEB-DL.x265.10bit.HDR.DDP5.1-KOGi",
"magnet:?xt=urn:btih:e2bbc743d0acaee338b30bf38d27d6b5af641532",
"复制磁力链接后打开 迅雷、utorrent、Bitcomet等进行下载！",
"【全银幕】The.Servant.1963.FS.2160p.BluRay.REMUX.HEVC.DTS-HD.MA.2.0-FGT【42.62 GB】",
"magnet:?xt=urn:btih:1d8b6b5ebb43d1b98374e0c6b255c5029f8595c5",
"复制磁力链接后打开 迅雷、utorrent、Bitcomet等进行下载！",
"③The.Servant.1963.OAR.2160p.UHD.BluRay.x265.10bit.HDR.FLAC.2.0-GUHZER【27.78 GB】",
"magnet:?xt=urn:btih:8770144d789e400cf9baa3604081291d63314e70",
"复制磁力链接后打开 迅雷、utorrent、Bitcomet等进行下载！",
"①Reign.of.the.Supermen.2019.2160p.BluRay.REMUX.HEVC.DTS-HD.MA.5.1-FGT【42.5GB】",
"magnet:?xt=urn:btih:TI5UQTZXPT5CUCSIDRAJF3MDMJCEHTZV",
"复制磁力链接后打开 迅雷、utorrent、Bitcomet等进行下载！",
"③Reign.of.the.Supermen.2019.2160p.UHD.BluRay.x265.10bit.HDR.DTS-HD.MA.5.1-SWTYBLZ【5.06G】",
"magnet:?xt=urn:btih:ISKPX53BRUAXZH7L6XQRB5BJLFBFTGI4",
"复制磁力链接后打开 迅雷、utorrent、Bitcomet等进行下载！",
"④Reign.of.the.Supermen.2019.2160p.BluRay.x264.8bit.SDR.DTS-HD.MA.5.1-SWTYBLZ【12.0GB】",
"magnet:?xt=urn:btih:WOGIB5MXAKOA7GMQH26ICZGFUUIA6Y5V",
"复制磁力链接后打开 迅雷、utorrent、Bitcomet等进行下载！",
"⑤Reign.of.the.Supermen.2019.2160p.BluRay.x265.10bit.SDR.DTS-HD.MA.5.1-SWTYBLZ【6.98GB】",
"magnet:?xt=urn:btih:UO4PNCSDFLG7AWVZQPYQAGAM22VL2BFJ",
"复制磁力链接后打开 迅雷、utorrent、Bitcomet等进行下载！",
"①Spider-Man.No.Way.Home.2022.2160p.BluRay.REMUX.HEVC.TrueHD.7.1.Atmos-FraMeSToR【61.50GB】",
"magnet:?xt=urn:btih:90e8be9013fa101b68478da3ac62c3d20a84b59b",
"点击或者复制磁力链接后打开迅雷、utorrent、Bitcomet等进行下载！",
"Spider-Man.No.Way.Home.2021.2160p.BluRay.REMUX.HEVC.DTS-HD.MA.TrueHD.7.1.Atmos-FGT【70.95 GB】",
"原盘REMUX3月24日更新",
"magnet:?xt=urn:btih:35d8b9167025854b7cc55663321f5061e3005766",
"③Spider-Man.No.Way.Home.2021.2160p.UHD.BluRay.x265.10bit.HDR.DTS-HD.MA.TrueHD.7.1.Atmos【21.47 GB】",
"magnet:?xt=urn:btih:18ee5f372e17f2943dcbc3e046557d0e83ffaffa",
"④Spider-Man.No.Way.Home.2021.2160p.BluRay.x264.8bit.SDR.DTS-HD.MA.TrueHD.7.1.Atmos【26.07 GB】",
"magnet:?xt=urn:btih:561fa9750cb34378e78b0a74b37a0f6653624b9f",
"⑤Spider-Man.No.Way.Home.2021.2160p.BluRay.x265.10bit.SDR.DTS-HD.MA.TrueHD.7.1.Atmos【25.10 GB】",
"magnet:?xt=urn:btih:3f9a2c89680923ceaf42e55fc7606d104837424e"
]
import re
m = {}
for magnet in range(len(test)):
    if test[magnet].startswith('magnet:?xt'):
        for index in range(5,0,-1):
            if re.findall('①|②|③|④|⑤|⑥|⑦|⑧|⑨|⑩|【|】|2160p|1080P',test[magnet-index]):
                m[test[magnet-index]] = test[magnet]
                break
            if index == 1:
                m[test[magnet - 1]] = test[magnet]
print(m)