class NewStack:

	def __init__(self, siz):
		top = 0
		Stck = []*siz

	def NewPush(element):
		if top<siz:
			stck[top] = element
			top += 1
			print("Item pushed")
		else:
			print("Stack Overflow")

	def NewPop(element):
		if top > -1:
			top -= 1
			return stck[top+1]
		else:
			return "Stack Underflow"


st = NewStack(5)
st.NewPush(6)
st.NewPush(7)
st.NewPush(8)
st.NewPush(9)
st.NewPush(10)
st.NewPush(11)
st.NewPop(10)
st.NewPush(11)






		

