import unittest

from unittest.mock import patch
from content_creatory import get_content
from content_creatory import create_mind_map


class TestSum(unittest.TestCase):

    def test_sum(self):
        content_with_html = '''
        <style>.card {
 font-family: SimSunl;
 font-size: 24px;
 text-align: center;
 color: black;
 background-color: white;
}
</style><span style="font-size: 42px; ">Nenne Lernorte der betrieblichen Ausbildung</span>

<hr id=answer>

<span style="font-family: SimSun; font-size: 70px; ">Betrieb und Berufschule</span>
        '''

        self.assertEqual(['Nenne Lernorte der betrieblichen Ausbildung', 'Betrieb und Berufschule'],
                         get_content(content_with_html))

        real_content_example = '''
<style>.card {
 font-family: SimSunl;
 font-size: 24px;
 text-align: center;
 color: black;
 background-color: white;
}
</style><span style="font-size: 42px; ">Ausnahme<b></b></span>

<hr id=answer>

<span style="font-family: SimSun; font-size: 70px; "><a href="https://dict.leo.org/chinesisch-deutsch/%E4%BE%8B%E5%A4%96"><font color="#ffffff">例外</font></a><div><a href="https://dict.leo.org/chinesisch-deutsch/l%C3%ACw%C3%A0i" style=""><font color="#ffffff">lìwài</font></a></div></span>
'''

        self.assertEqual(['Ausnahme', '例外', 'lìwài'],
                         get_content(real_content_example))

        real_content_multiple = '''
<style>.card {
 font-family: SimSunl;
 font-size: 24px;
 text-align: center;
 color: black;
 background-color: white;
}
</style><span style="font-size: 42px; ">unverstellbar, nicht vorstellbar, unglaublich, es ist schwer sich so etwas vorzustellen</span>

<hr id=answer>

<span style="font-family: SimSun; font-size: 70px; ">难以想象<div>nán yǐ xiǎng xiàng<br></div></span>
        '''

        self.assertEqual(['unverstellbar, nicht vorstellbar, unglaublich, es ist schwer sich so etwas vorzustellen',
                          '难以想象',
                          'nán yǐ xiǎng xiàng'],
                         get_content(real_content_multiple))

    @patch("content_creatory.get_content")
    def test_create_mind_map(self, get_content_mock):
        get_content_mock.return_value = ['Ausnahme', '例外', 'lìwài']
        create_mind_map("ignored")

    @patch("content_creatory.get_content")
    def test_create_mind_map_multiple(self, get_content_mock):
        get_content_mock.return_value = ['unverstellbar, nicht vorstellbar, unglaublich, es ist schwer sich so etwas vorzustellen',
                          '难以想象',
                          'nán yǐ xiǎng xiàng']
        create_mind_map("ignored")


if __name__ == '__main__':
    unittest.main()
