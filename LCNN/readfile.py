import os

filelist=[]
labellist=[]
path = "LA/ASVspoof2019_LA_train_orig/flac"
labelpath ="data_LAbkp/trn_dev_eval_scps/ASVspoof2019.LA.cm.train.trn.txt"


for file in os.listdir(path):
	filelist.append(file)


#print(filelist)
#print(len(filelist))

ctr_spoof=0
ctr_bon=0
with open(labelpath, 'r') as myfile:
	for line in myfile:
		print(line)
		labellist.append(line)
		parts= line.split(' ')
		print("parts--", parts)
		if(parts[-1].strip() == 'spoof'):
			ctr_spoof+=1
		else:
			ctr_bon +=1	
print(len(filelist))
print(len(labellist))
print(ctr_spoof, ctr_bon)
