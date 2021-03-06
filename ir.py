# coding=utf-8

import sys, json, random
# import src.test

count = 0

# Read data from stdin
def read_in():
    line = sys.stdin.readline()
    return json.load(line)

# random generate a json
def gen():
    global count

    # parameter
    TOPIC_NUM = 12
    PAIRS_NUM = 6

    # {index: 1, docs:[ [a,b],[a,b],[a,b], ...] }
    topic_indices = random.sample(range(TOPIC_NUM), PAIRS_NUM).sort()
    question = { 'index': count, 'docs': [] }
    for topic_index in topic_indices:
        question['docs'].append(genRandomDocInTopic(topic_index))

    count += 1
    return question

# randomly gen a doc in this topic
# @return: string, text of this random doc
def genRandomDocInTopic(topic_index):
    #TODO
    return src.test.genRandomDocInTopic(topic_index)

def evaluate( data ):
    # data = {index: 1, input: ["我喜歡","jhk",...]}
    # this program should store which index store what docs
    # by the index and the choice seq 010101001
    # this function returns the result: [0.5, 0.0, 0.12, 0.3, 0.04, 0.04]
    return src.test.predict_user( data["input"] , method = "KNN" )

def main():
	global count

	sys.stderr.write(' >>>>>>  IR server runed \n')
	sys.stderr.flush()

	# jieba.set_dictionary( 'dict.txt.big' )

	# get our data as an array from read_in()
	for line in sys.stdin:
		key = line.split()[0]

		if key == 'Load': # 0

			sys.stderr.write( 'Loading data #' + str(count) + '\n' )	
			print( '0 ' + json.dumps( gen() ) )

		elif key == 'Eva': # 1

			line = line.replace( 'Eva ', '', 1 )[:-1]
			obj = json.loads( line )
			sys.stderr.write( 'Evaluate data #' + str(obj[ 'index' ]) + ': input length ' + str(len(obj[ 'input' ])) + '\n' )
			print( '1 ' + json.dumps( evaluate( obj ) ) )

		else:
			sys.stderr.write( 'Got invalid: ' + line )

		sys.stderr.flush()
		sys.stdout.flush()
		
	sys.stderr.write('******************************\n')	
	sys.stderr.write(' >>>>>>  IR server finished \n')
	sys.stderr.write('******************************\n')	

#start process
if __name__ == '__main__':
    main()

