import numpy as np, subprocess
from scipy.io import wavfile
from scipy.signal import lfilter, butter
SR=48000
TOTAL=47.5
rng=np.random.default_rng(11)
post=lambda T:T
n_tot=int(round(TOTAL*SR))
# ---------- synth
buf=np.zeros((2,n_tot+SR*3),dtype=np.float64)
def put(sig,T,pan=0.0,gain=1.0):
    # sig mono; pan -1..1
    t0=int(post(T)*SR)
    if t0<0: return
    l=np.cos((pan+1)*np.pi/4);r=np.sin((pan+1)*np.pi/4)
    n=min(len(sig),buf.shape[1]-t0)
    buf[0,t0:t0+n]+=sig[:n]*gain*l*1.414; buf[1,t0:t0+n]+=sig[:n]*gain*r*1.414
def tt(d): return np.arange(int(d*SR))/SR
def lp_sweep(x,f0,f1):
    n=len(x); fc=np.geomspace(f0,f1,n); a=1-np.exp(-2*np.pi*fc/SR)
    y=np.zeros(n); s=0.0
    for i in range(n):
        s+=a[i]*(x[i]-s); y[i]=s
    return y
def whoosh(dur,f0=500,f1=5500,peak=0.4,hp=220):
    n=int(dur*SR); x=rng.standard_normal(n)
    y=lp_sweep(lp_sweep(x,f0,f1),f0*1.3,f1*1.3)
    b,a=butter(2,hp/(SR/2),'high'); y=lfilter(b,a,y)
    x01=np.linspace(0,1,n); env=np.sin(np.pi*x01**peak)**2
    y*=env; y/=np.abs(y).max()+1e-9
    return y
def pluck(f,dur=0.5):
    t=tt(dur); y=np.sin(2*np.pi*f*t)*np.exp(-t/0.11)+0.3*np.sin(2*np.pi*2*f*t)*np.exp(-t/0.06)+0.12*np.sin(2*np.pi*3.01*f*t)*np.exp(-t/0.03)
    y*=np.minimum(1,t/0.003); return y/np.abs(y).max()
def tick(f,dur=0.05):
    t=tt(dur); return np.sin(2*np.pi*f*t)*np.exp(-t/0.007)*np.minimum(1,t/0.0008)
def click():
    t=tt(0.06); nz=rng.standard_normal(len(t)); b,a=butter(2,2500/(SR/2),'high'); nz=lfilter(b,a,nz)*np.exp(-t/0.0018)
    th=np.sin(2*np.pi*190*t)*np.exp(-t/0.012)
    y=0.7*nz+0.9*th+0.3*np.sin(2*np.pi*1700*t)*np.exp(-t/0.004); return y/np.abs(y).max()
def ding(f=1318.5,dur=1.3):
    t=tt(dur); y=np.sin(2*np.pi*f*t)*np.exp(-t/0.45)+0.35*np.sin(2*np.pi*2.76*f*t)*np.exp(-t/0.18)+0.2*np.sin(2*np.pi*f*1.5*t)*np.exp(-t/0.3)
    y*=np.minimum(1,t/0.004); return y/np.abs(y).max()
def thump(dur=1.2):
    t=tt(dur); f=42+70*np.exp(-t/0.12); ph=2*np.pi*np.cumsum(f)/SR
    y=np.sin(ph)*np.exp(-t/0.35)
    nz=rng.standard_normal(len(t)); b,a=butter(2,260/(SR/2)); nz=lfilter(b,a,nz)*np.exp(-t/0.06)
    y=y+0.5*nz; y*=np.minimum(1,t/0.002); return y/np.abs(y).max()
def shimmer(dur=1.8):
    t=tt(dur); y=np.zeros_like(t)
    for i,f in enumerate([2093,2637,3136,3951,4186]):
        d=0.04*i; tau=0.7+0.1*i
        y+=np.sin(2*np.pi*f*t)*np.exp(-np.maximum(t-d,0)/tau)*np.minimum(1,np.maximum(t-d,0)/0.01)
    return y/np.abs(y).max()
def swell(dur=2.0,freqs=(261.6,329.6,392.0,523.3)):
    t=tt(dur); y=np.zeros_like(t)
    for f in freqs:
        y+=np.sin(2*np.pi*f*t)+0.5*np.sin(2*np.pi*f*1.003*t)
    env=np.sin(np.pi*np.linspace(0,1,len(t)))**2; y*=env; return y/np.abs(y).max()
def scan(dur=2.0):
    t=tt(dur); f=380*np.exp(np.log(1500/380)*t/dur); ph=2*np.pi*np.cumsum(f)/SR
    y=np.sin(ph)*(0.6+0.4*np.sin(2*np.pi*11*t)); env=np.sin(np.pi*np.linspace(0,1,len(t)))**1.3
    return y*env/np.abs(y*env).max()
