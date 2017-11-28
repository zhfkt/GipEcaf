import os, sys

import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

result_file = open("./PigIdentification3.csv", "w+")
result_file.truncate()
print("result file: ", result_file.name)

# change this as you see fit
image_folder_path = sys.argv[1]

# Unpersists graph from file
with tf.gfile.FastGFile("retrained_graph3.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')


with tf.Session() as sess:
    # Feed the image_data as input to the graph and get first prediction
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

for parent, dirnames, filenames in os.walk(image_folder_path):
    for filename in filenames:
        image_name = filename.split('.')[0]
        image_path = image_folder_path +'/' + filename
        print("image: ", image_path)
        # Read in the image_data
        image_data = tf.gfile.FastGFile(image_path, 'rb').read()

        # Loads label file, strips off carriage return
        label_lines = [line.rstrip() for line 
                           in tf.gfile.GFile("retrained_labels.txt")]

        predictions = sess.run(softmax_tensor, \
                 {'DecodeJpeg/contents:0': image_data})
        
        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        
        for idx, node_id in enumerate(top_k):
            human_string = label_lines[node_id]
            if idx == 0:
                score = ("%.9f" % 1)
            else:
                score = ("%.9f" % 0)
            #score = ("%.9f" % predictions[0][node_id])
            # print('%s (score = %.5f)' % (human_string, score))
            result_file.write(str(image_name) + ',' + str(human_string) + ',' + str(score) + '\n')
        result_file.flush()

result_file.close()
