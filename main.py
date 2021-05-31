import random

from fastapi import FastAPI
app = FastAPI()

#www.almaty.kz
#www.almaty.kz/news/
#www.almaty.kz/news/alatau/
#www.almaty.kz/news/alatau/today#


@app.get("/")
def home():
	return "Bul ui paragshasi"

@app.get("/news")
def news():
	return "bul janalig paragshasi"

@app.get("/quotes")
def quotes():
	quotes = [
	"Öz isiñniñ bilgiri häm şeberi atanw üşin jaqsı jumıs istep, jetik bilwge umtılw kerek. Qanday äreket jasap, qanday is ister bolsañız da – ïgiligin körip, raxatına bölenwdi maqsat tutqan jön.",
	"Dünïyedegi eñ oñay närse — kisige aqıl aytw, eñ qïını öziñdi-öziñ tüsinw.",
	"Ğaqlïya közben qarasañ, Dünïye – ğajap, sen – esik. Jahlı közben qarasañ, Dünïye – qoqıs, sen – menşik.",
	
	]

	result = random.choice(quotes)
	return result
	


