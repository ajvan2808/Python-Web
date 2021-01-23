from flask import Flask

app = Flask(__name__)

import Package_Module_1.app_bai_1
import Package_Module_1.app_bai_2
import Package_Module_1.app_bai_3
import Package_Module_1.app_Trang_chu
import Package_Module_1.app_bai_4
import Package_Module_1.app_bai_5

'''				Package trong Python  			
- Package là 1 thư mục có thể chứa 1 hoặc nhiêù modules hay các package khác nhau 
- Được tạo ra nhằm để quản lý những modules, thư mục có cùng mục đích. Để dễ dàng quản lý source code.
- Build package: 
	+ Trong package nhất định phải có 1 file __init__.py 
	+ Đây có thể coi là constructor hoặc file đại diện, quản lý cho package này. Khi import package vào 1 thư mục cùng cấp init sẽ được gọi ra đầu tiên.
- 1 package có thể chứa 1 package khác tuy nhiên vẫn cần phải tuân thủ mỗi pk chứa 1 file __init__.py
'''
