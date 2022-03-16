import streamlit as st
import random
from lfu import *



st.header("Least Frequently Used (LFU) Cache Implementation.")

st.sidebar.title('LFU Cache Implementation')
st.sidebar.write('Least Frequently Used (LFU) is a caching algorithm in which the least frequently used cache block is removed whenever the cache is overflowed.')

st.sidebar.write('Kerwin Umpay')


cache = LFUCache(2)
st.write('Capacity is 2')


st.write("Insert Key 1")
val1 = st.slider('Select', 0, 50, 25,key=1)
cache.put(1, val1)
st.write('Key 1:',val1)
st.write("Insert Key 2")
val2 = st.slider('Select', 0, 50, 25,key=2)
cache.put(2, val2)
st.write('Key 2:',val2)




st.write(' Get Key 1 :',cache.get(1)) 



st.write("Insert Key 3") 
val3 = st.slider('Select', 0, 50, 25,key=3)
cache.put(3, val3)  
st.write('Key 3:',val3)


st.write('Get Key 2 :',cache.get(2))
 
st.write('Get Key 3 :',cache.get(3)) 



st.write("Insert Key 4")
val4 = st.slider('Select', 0, 50, 25,key=4)
cache.put(4, val4) 
st.write('Key 4:',val4)




st.write(' Get Key 1 :',cache.get(1)) 
st.write('Get Key 2 :',cache.get(2)) 
st.write('Get Key 3 :',cache.get(3)) 
st.write('Get Key 4 :',cache.get(4)) 

# cache = LFUCache(2)
# st.write("Insert Key 1")
# cache.put(1, 1)
# st.write("Insert Key 2")
# cache.put(2, 2)
# st.write(cache.get(1))  
# st.write("Insert Key 3")    
# cache.put(3, 3)  
# st.write("Get Key 2")
# st.write(cache.get(2))
# st.write("Get Key 3")   
# st.write(cache.get(3)) 

# st.write("Insert Key 4")
# cache.put(4, 4)  
# st.write("Get Key 1")  
# st.write(cache.get(1)) 
# st.write("Get Key 3")   
# st.write(cache.get(3))

    