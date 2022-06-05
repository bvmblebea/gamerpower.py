from requests import get



class GamerPower:
	def __init__(self):
		self.api = "https://www.gamerpower.com/api"
		self.headers = {
			"User-Agent": "Mozilla/5.0 (Linux; Android 11; RMX2086 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36"
		}
	
	def get_giveaways(self):
		return get(f"{self.api}/giveaways", headers=self.headers).json()
	
	def get_giveaways_by_platform(self, platform: str = "pc"):
		return get(
			f"{self.api}/giveaways?platform={platform}",
			headers=self.headers).json()
	
	def get_giveaways_by_type(self, type: str = "game"):
		return get(
			f"{self.api}/giveaways?type={type}", headers=self.headers).json()
	
	def sort_giveaways(self, sort: str):
		return get(
			f"{self.api}/giveaways?sort-by={sort}",
			headers=self.headers).json()
	
	def get_giveaways_by_all(
			self,
			platform: str = "steam",
			type: str = "loot",
			sort: str = "popularity"):
		return get(
			f"{self.api}/giveaways?platform={platform}&type={type}&sort-by={sort}",
			headers=self.headers).json()
		
	def get_giveaway_details(self, giveaway_id: int):
		return get(
			f"{self.api}/giveaway?id={giveaway_id}",
			headers=self.headers).json()
	
	def filter_giveaway(
			self,
			platform: str = "epic-games-store.steam.android",
			type: str = "game.loot"):
		return get(
			f"{self.api}/filter?platform={platform}&type={type}",
			headers=self.headers).json()
	
	def get_total_giveaways_worth(self):
		return get(
			f"{self.api}/worth", headers=self.headers).json()
