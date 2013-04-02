from jap.skel import skel

def test_stuff():
  assert skel.a(5) == 15

#def test_stuff_fail():
#  assert skel.a(6) == 17

import time
def fake_time():
  return 1364423661.330722


def test_time(monkeypatch):
  monkeypatch.setattr(time, 'time', fake_time)
  
  now = time.time()    
  assert now == 1364423661.330722

def test_time_real():
  now = time.time()
  assert now > 1364423661.330722
  