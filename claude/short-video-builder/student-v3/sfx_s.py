exec(open('/home/claude/vert2/synth.py').read())
W=lambda T,d,f0,f1,g,pan=0.0,pk=0.55: put(whoosh(d,f0,f1,pk),T,pan,g)
def typing(t0,t1,every,g=0.03):
    T=t0
    while T<t1:
        put(tick(1500+int(rng.integers(0,700))),T,float(rng.uniform(-.2,.2)),g*float(rng.uniform(.7,1.2)));T+=every*float(rng.uniform(.8,1.25))
W(0.15,0.8,400,5000,0.10)                       # draft card in
for T,f in [(3.8,784),(4.7,880),(5.3,988)]: W(T,0.35,900,5500,0.05,0.2,0.5); put(pluck(f),T+.2,0.3,0.07)
W(5.9,0.8,400,4500,0.10,-0.3)                   # presenter out, card up
W(6.4,0.6,400,3500,0.08)                        # prompt bar in
typing(7.55,8.85,0.075); put(click(),8.95,0,0.14)
typing(9.7,10.75,0.06); put(click(),11.15,0,0.14)
put(pluck(392),11.85,0,0.07)                    # still the same draft
W(15.45,0.9,350,6000,0.14)                      # do this instead
put(pluck(587),17.35,0,0.06)
W(18.15,0.5,500,4500,0.08,-0.2); put(pluck(659.3),18.25,0,0.09)
W(19.05,0.5,500,4500,0.08,0.2); put(pluck(784),19.15,0,0.09)
W(21.35,0.7,400,4500,0.09)                      # tracker
W(22.05,0.7,400,4500,0.10)                      # prompt card
typing(22.8,24.3,0.04,0.022)
for T,f in [(27.6,523.3),(28.4,659.3),(29.0,784.0)]: put(pluck(f),T,0,0.08); W(T-0.05,0.35,900,5500,0.04,0.2,0.5)
W(29.6,0.7,400,4500,0.09,-0.3)                  # card out
W(30.25,0.8,400,5000,0.12,0.2)                  # UI in
put(pluck(659.3),30.5,0,0.07)
typing(31.2,32.6,0.03,0.03)
put(click(),36.05,0,0.16)
typing(37.6,39.3,0.04,0.02)
for T,f in [(37.5,523.3),(37.62,659.3),(37.74,784.0)]: put(pluck(f),T,0,0.09)
W(39.3,0.4,900,5500,0.05,-0.3,0.5); W(39.35,0.4,900,5500,0.05,0.3,0.5); put(pluck(880),39.55,0.3,0.07)
put(swell(1.9),38.6,0,0.04); put(shimmer(1.6),39.2,0,0.035)
W(40.2,0.7,400,4500,0.10,0.3)                   # UI out
W(40.25,0.7,400,4500,0.10,-0.3)                 # presenter in
W(40.85,0.7,400,4500,0.09,0.3)                  # card in
put(scan(1.4),41.4,0,0.025)
for i in range(8): put(pluck(660+60*i,0.35),44.6+i*0.3,0,0.04)
put(ding(1318.5),47.0,0,0.05); put(shimmer(1.8),47.0,0,0.04)
sf=buf[:,:n_tot]
b,a=butter(2,60/(SR/2),'high'); sf=lfilter(b,a,sf,axis=1)
print('sfx peak',np.abs(sf).max())
wavfile.write('/home/claude/vert2/sfx.wav',SR,sf.T.astype(np.float32))
