
class Button:
    _click_count = 0
    def click(self):
        self._click_count += 1
    def reset(self):
        self._click_count = 0
    def click_count(self):
        print(self._click_count)
btn = Button()
btn.click_count()
btn.click()
btn.click_count()
btn.reset()
btn.click_count()