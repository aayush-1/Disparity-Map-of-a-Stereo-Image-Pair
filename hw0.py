import cv2
import numpy as np
import matplotlib.pyplot as plt


leftimage = cv2.imread('HW0-left.png')  
rightimage = cv2.imread('HW0-right.png')
leftimage = cv2.cvtColor(leftimage, cv2.COLOR_BGR2GRAY)/255
rightimage = cv2.cvtColor(rightimage, cv2.COLOR_BGR2GRAY)/255

# cv2.imshow('image 1', leftimage)
# cv2.imshow('image 2', rightimage)
# # cv2.imshow('im',leftimage-rightimage)

# print((left-right))

left=leftimage[28:228,28:228]
right=rightimage[28:228,28:228]
# print(left.shape)
# cv2.imshow('image 3', left[28:100][28:228])
# # cv2.imshow('image 4', right)
# cv2.waitKey(5000)

# print(len(left[0]))0
disparity_range=[0,1,2,3,4,5,6,7,8,9]
gamma=2
k=2
d0=7
a=[[-1,0],[0,1],[1,0],[0,-1]]
mu=np.zeros((200,200))
output=np.zeros((200,200))

for i in range(len(left)):
	print(i)
	for j in range(len(left[i])):
		# si_s=np.zeros(len(disparity_range))
		for ds in disparity_range:
			# print((leftimage[28+i,28+j]-rightimage[28+i+ds,28+j])**2)
			si_s=np.exp(-(1/(2*gamma**2))*(leftimage[28+i,28+j]-rightimage[28+i+ds,28+j])**2)
			m_ts=np.zeros(4)
			for dt in disparity_range:
				for z in  range(4):
					m_ts[z]+=np.exp(-(1/(2*gamma**2))*min((ds-dt)**2,d0**2))*(np.exp((-1/(2*gamma**2))*(leftimage[28+i+a[z][0],28+j+a[z][1]]-rightimage[28+i+dt+a[z][0],28+j+a[z][1]])**2))
			temp=k*si_s*m_ts[0]*m_ts[1]*m_ts[2]*m_ts[3]
			if (temp>mu[i,j]):
				output[i,j]=ds
				mu[i,j]=temp


plt.imshow(output)
plt.show()