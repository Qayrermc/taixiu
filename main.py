#author: Qayrermc
#name: hệ thống tài xỉu 
#version: 1.0
#created: 5/6/2024
import random
print("-----------------------------")
print(" CHƯƠNG TRÌNH TÀI XỈU ")
print("-----------------------------")
print(" ")
print("vui lòng chọn kết quả dự đoán")
print("tài hoặc xỉu")
ketqua = input()
if ketqua !="tài" and ketqua !="xỉu":
  print("vui lòng nhập đúng tài hoặc xỉu")
  ketqua= input()
print("bạn đã chọn",ketqua)
print("nhập số tiền cược")
s = input()
s = int(s)
print("bạn đã cược:",ketqua,":",s)

x = random.randrange(1,7)
y= random.randrange(1,7)
z = random.randrange(1,7)
num = x + y*3 + z*2
if num % 2 == 0:
 
  print("ra xỉu")
else:

  print("ra tài")
if ketqua =="xỉu" and num % 2 == 0:
  print("bạn đã thắng và x2 số tiền cược",s*2)
if ketqua =="tài" and num % 2 != 0:
  print("bạn đã thắng và x2 số tiền cược",s*2)
if ketqua =="xỉu" and num % 2 != 0:
  print("bạn đã thua và mất đi số tiền cược")
if ketqua =="tài" and num % 2 == 0:
  print("bạn đã thua và mất đi số tiền cược")
print(" ")
print("bạn có muốn chơi tiếp không: có/không")
choitiep = input()
if choitiep != "có" and choitiep != "không":
  print("vui lòng nhập đúng có hoặc không")
while choitiep == "có":
  print("vui lòng chọn kết quả dự đoán")
  print("tài hoặc xỉu")
  ketqua = input()
  if ketqua !="tài" and ketqua !="xỉu":
    print("vui lòng nhập đúng tài hoặc xỉu")
    ketqua= input()
  print("bạn đã chọn",ketqua)
  print("nhập số tiền cược")
  s = input()
  s = int(s)
  print("bạn đã cược:",ketqua,":",s)

  x = random.randrange(1,7)
  y= random.randrange(1,7)
  z = random.randrange(1,7)
  num = x + y*3 + z*2
  if num % 2 == 0:

    print("ra xỉu")
  else:

    print("ra tài")
  if ketqua =="xỉu" and num % 2 == 0:
    print("bạn đã thắng và x2 số tiền cược",s*2)
  if ketqua =="tài" and num % 2 != 0:
    print("bạn đã thắng và x2 số tiền cược",s*2)
  if ketqua =="xỉu" and num % 2 != 0:
    print("bạn đã thua và mất đi số tiền cược")
  if ketqua =="tài" and num % 2 == 0:
    print("bạn đã thua và mất đi số tiền cược")
  print(" ")
  print("bạn có muốn chơi tiếp không: có không")
  choitiep = input()
  if choitiep != "có" and choitiep != "không":
    print("vui lòng nhập đúng có hoặc không")
