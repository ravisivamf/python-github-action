class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

r = requests.get('https://weather.talkpython.fm/api/weather?city=irving&state=TX&country=US&units=imperial')
if r.status_code == 200:
   data = r.json()
   temperature = data["forecast"]["temp"]
   print(f'Weather in Irving, TX: {temperature}')
