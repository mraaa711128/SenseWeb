from django.http import JsonResponse
from Utility import telerivet

API_KEY = "sgA1AXcGjRAI5lbsmzPcISeYEtQuiFGa"
PROJECT_ID = "PJf2f77067684eae19"

def sendmessage(request,phonenum):
	try:
		tel = telerivet.API(API_KEY)
		pj = tel.initProjectById(PROJECT_ID)

		ct = pj.getOrCreateContact(phone_number=phonenum)
		srv_cur = pj.queryServices(name="Cld_NewArriveIntro")
		srv = srv_cur.next()
		st = srv.getContactState(ct)
		if ct.name == phonenum:
			if st.id == None:
				srv.setContactState(contact=ct,id='intro')

				pj.sendMessage(content="Hi, We are Sense, your live Netflix assistant. So, I believe you want to watch a movie without digging into a deep investigation, right? So, how about let us know your NAME and TWITTER account first? Send us in the following format: YourName @Twitter",
							   to_number=phonenum)
			else:
				srv.setContactState(contact=ct,id='requestname')

				pj.sendMessage(content="Hi, we seem had a little chat before. Do you want to know more about Sense? How about let me know your name first by replying: YourName @Twitter",
							   to_number=phonenum)
		else:
			if st.id == 'pick':
				srv.setContactState(contact=ct,id='return')

				pj.sendMessage(content="Cool! To get started, can you give me a movie you like and a few reasons why? I\'ll use this as the basis for your first pick! Or you can reply \"BuzzFeed\" to do a little quiz to let us know more about you!",
							   to_number=phonenum)
			else:
				pj.sendMessage(content="Hi " + ct.name + ", how's the last movie recommendation? Do you want us to give you another one for today? ",
							   to_number=phonenum)

		return JsonResponse({'status':'success','telnum':phonenum,'':''})
	except Exception, e:
		return JsonResponse({'status':'fail','message':str(e)})
