import pytest

from django_py_reverse.urls import Urls


class TestUrls:
    URLS = {
        "urls": [
            [
                "account_confirm_email",
                [["accounts/confirm_email/%(key)s/", ["key"]]],
            ],
            ["account_delete", [["accounts/delete/", []]]],
            ["account_password_reset", [["es/accounts/password/reset/", []]]],
            [
                "account_password_reset_token",
                [
                    [
                        "accounts/password/reset/%(uidb36)s-%(token)s/",
                        ["uidb36", "token"],
                    ]
                ],
            ],
        ],
        "prefix": "/",
    }

    API_ENDPOINT = "https://example.com"

    @pytest.mark.parametrize(
        "url_pattern, expected, key",
        [
            (
                "account_confirm_email",
                "/accounts/confirm_email/some-token/",
                {"key": "some-token"},
            ),
            (
                "account_delete",
                "/accounts/delete/",
                {},
            ),
            (  # This one has language
                "account_password_reset",
                "/es/accounts/password/reset/",
                {},
            ),
            (
                "account_password_reset_token",
                "/accounts/password/reset/uidb36-token/",
                {"uidb36": "uidb36", "token": "token"},
            ),
        ],
    )
    def test_get_url(self, url_pattern: str, expected: str, key: dict) -> None:
        urls = Urls(self.URLS).factory()

        url = urls[url_pattern](**key)

        assert url == expected

    @pytest.mark.parametrize(
        "url_pattern, expected, key",
        [
            (
                "account_confirm_email",
                "https://example.com/accounts/confirm_email/some-token/",
                {"key": "some-token"},
            ),
            (
                "account_delete",
                "https://example.com/accounts/delete/",
                {},
            ),
            (  # This one has language
                "account_password_reset",
                "https://example.com/es/accounts/password/reset/",
                {},
            ),
            (
                "account_password_reset_token",
                "https://example.com/accounts/password/reset/uidb36-token/",
                {"uidb36": "uidb36", "token": "token"},
            ),
        ],
    )
    def test_get_url_with_custom_prefix(
        self, url_pattern: str, expected: str, key: dict
    ) -> None:
        urls = Urls(self.URLS, self.API_ENDPOINT).factory()

        url = urls[url_pattern](**key)

        assert url == expected

    @pytest.mark.parametrize(
        "url_pattern, expected, key",
        [
            (
                "account_confirm_email",
                "/accounts/confirm_email/some-token/",
                {"key": "some-token"},
            ),
            (
                "accountConfirmEmail",
                "/accounts/confirm_email/some-token/",
                {"key": "some-token"},
            ),
        ],
    )
    def test_get_url_with_js_style(
        self, url_pattern: str, expected: str, key: dict
    ) -> None:
        urls = Urls(self.URLS, include_js_style=True).factory()

        url = urls[url_pattern](**key)

        assert url == expected

    def test_get_url_with_invalid_key(self) -> None:
        urls = Urls(self.URLS).factory()

        url = urls["account_confirm_email"](keys="some-token")

        assert url is None

    def test_get_url_with_inexistent_url(self) -> None:
        urls = Urls(self.URLS).factory()

        with pytest.raises(KeyError):
            urls["inexistent_url"]()

    def test_get_url_prefix_without_ending_slash(self) -> None:
        urls = Urls(
            {
                "urls": [
                    ["account_delete", [["accounts/delete/", []]]],
                ],
                "prefix": "/",
            },
            url_prefix="es",
        ).factory()

        assert urls["account_delete"]() == "es/accounts/delete/"
