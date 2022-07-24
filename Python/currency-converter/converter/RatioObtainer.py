import json, datetime, urllib.request, os


class RatioObtainer:
    base = None
    target = None

    def __init__(self, base, target):
        self.base = base
        self.target = target

    def was_ratio_saved_today(self):
        # TODO
        # This function checks if given ratio was saved today and if the file with ratios is created at all
        # should return false when file doesn't exist or if there's no today's exchange rate for given values at all
        # should return true otherwise
        
        if not os.path.exists('./ratios.json'): return False
        
        with open('./ratios.json') as data:
            ratios = json.load(data)
            found = False
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            for r in ratios:
                if r['base_currency'] == self.base and r['target_currency'] == self.target and r['date_fetched'] == date:
                    found = True
                    break

        return found

    def fetch_ratio(self):
        # TODO
        # This function calls API for today's exchange ratio
        # Should ask API for today's exchange ratio with given base and target currency
        # and call save_ratio method to save it

        url = f"https://api.exchangerate.host/convert?from={self.base}&to={self.target}"
        response = urllib.request.urlopen(url)
        ratio = json.loads(response.read())['info']['rate']
        
        self.save_ratio(ratio)

    def save_ratio(self, ratio):
        # TODO
        # Should save or update exchange rate for given pair in json file
        # takes ratio as argument
        # example file structure is shipped in project's directory, yours can differ (as long as it works)
        
        with open('./ratios.json', 'r') as data:
            ratios = json.load(data)
        for r in ratios:
            if r['base_currency'] == self.base and r['target_currency'] == self.target:
                r['ratio'] = ratio
                r['date_fetched'] = datetime.datetime.now().strftime("%Y-%m-%d")
                with open('./ratios.json', 'w') as file:
                    file.write(json.dumps(ratios))
                return
        ratios.append({
            "base_currency": self.base,
            "target_currency": self.target,
            "date_fetched": datetime.datetime.now().strftime("%Y-%m-%d"),
            "ratio": ratio
        })
        with open('./ratios.json', 'w') as file:
            file.write(json.dumps(ratios))              

    def get_matched_ratio_value(self):
        # TODO
        # Should read file and receive exchange rate for given base and target currency from that file
        
        with  open('./ratios.json') as data:
            ratios = json.load(data)
        for r in ratios:
            if r['base_currency'] == self.base and r['target_currency'] == self.target:
                return r['ratio']
                    