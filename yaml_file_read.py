import os
import io
import yaml

#print (os.listdir("."))
root_dir = "/Users/skarthi/yaml_source_files"
target_folder ="/Users/skarthi/yaml_target_folders"
for root, dirs, files in os.walk(root_dir):
	#print ("root is ",root)
	#print ("dirs is ",dirs)
	#print ("files is ",files)
	for file in files:
		if file.endswith(".yaml"):
			#print ("The file is ",file)
			source_dir = root_dir+"/"+file
			#print ("Source file is ",source_dir)
			with open(source_dir, 'r') as stream:
				data_loaded = yaml.load(stream)
				print ("Data in the yaml file is ",data_loaded)
				file_key_value = data_loaded["key_value"]
				print ("Key value in the input file {} is {}".format(source_dir,file_key_value))
				
				for root,dirs,files in os.walk(target_folder):
					for dir1 in dirs:
						print ("Directories inside target folders",dir1)
						tgt_child_dir = target_folder+"/"+dir1
						for root,dirs,files in os.walk(tgt_child_dir):
							for file in files:
								print ("Files inside target folder",file)
								if file.endswith(".yaml"):
									check_file = tgt_child_dir +"/"+file
									print ("Target file is ",check_file)
									with open(check_file, 'r') as stream1:
										data_loaded1 = yaml.load(stream1)                              
										print ("Data in the yaml file is ",data_loaded1)
										output_key_value = data_loaded1["key_value"]
										print (output_key_value)
										if file_key_value == output_key_value:
											print ("Key Value matches for file from source {} to target {} :{}".format(file_key_value,output_key_value,source_dir))
										else:
											print ("Key value didnt match so update the key_value")

											data_loaded1["key_value"]=file_key_value
											
											print ("printing updated dictionary", data_loaded1)
											with io.open(check_file, "w") as outfile:
												yaml.dump(data_loaded1, outfile)
												print ("value({}) updated in the file {} ".format(file_key_value,check_file))
