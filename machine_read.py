# -*- encoding: utf-8 -*-
# import os
# # os.system("echo 'hello world'")
# os.system("say 'hello world'")
from __future__ import unicode_literals

from gtts import gTTS
import os


text = """


br blbr bl
   brbbrr   brbbrr
brb  brb   bll brr   bllthr splthr spl
   spllspls   spllspls
spll  spll   thrr spls   thrtph scph sc
   scsscc   scsscc
scs  scs   phh scc   scs


wr smwr sm
   smmssmm   smmssmm
smms  smms   smms smm   smmshr strshr str
   shrrstrs   shrrstrs
shrr  shrr   shrs strs   strssk cksk ck
   ckkskk   ckkskk
ckk  ckk   ckc skk   sks


ymmy ymmy ymm ymy ymmyymmy
smms smms smm sms smmssmms
kzzk kzzk kzz kzk kzzkkzzk

br plbr pl
   pllpbrr   pllpbrr
pllp  pllp   brrb brr   brrspr scrspr scr
   sprrsprrps   sprrsprrps
sprr  sprr   scrrcs sprrps   sprrch ngch ng
   ngnchc   ngnchc
ngn  ngn   ngn chc   nggn


tr brtr br
   brrbtrt   brrbtrt
brrb  brrb   brb trt   brbspl shrspl shr
   shrrhsshrs   shrrhsshrs
shrrhs  shrrhs   shrs shrs   spllpsck shck sh
   shhckc   shhckc
shh  shh   ckk ckc   shhs


tmmt tmmt tmm tmt tmmttmmt
wddw wddw wdd wdw wddwwddw
krrk krrk krr krk krrkkrrk

cl stcl st
   cllcstt   cllcstt
cllc  cllc   clc stt   cllspr shrspr shr
   sprsshrr   sprsshrr
sprs  sprs   sprs shrr   shrrhssk phsk ph
   skksskk   skksskk
skks  skks   phh skk   php


sm trsm tr
   smmsmm   smmsmm
smm  smm   trrt smm   trrspl thrspl thr
   thrrhtspls   thrrhtspls
thrrht  thrrht   spll spls   thrtck ghck gh
   ckkckc   ckkckc
ckk  ckk   ckc ckc   ghh


whhw whhw whh whw whhwwhhw
mbbm mbbm mbb mbm mbbmmbbm
hxxh hxxh hxx hxh hxxhhxxh





"""

tts = gTTS(text= text, lang='en')
tts.save("audio/song_01.mp3")
