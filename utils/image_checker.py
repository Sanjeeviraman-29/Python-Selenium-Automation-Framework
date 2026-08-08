import requests


class ImageChecker:

    @staticmethod
    def check_image(url):

        try:

            response = requests.get(
                url,
                timeout=10
            )

            return response.status_code

        except Exception:

            return None