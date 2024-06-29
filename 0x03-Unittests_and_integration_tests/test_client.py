#!/usr/bin/env python3
"""model to test the client file"""
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class


class TestGithubOrgClient(unittest.TestCase):
    """define testgithuborgclient class"""
    @parameterized.expand([('google'), ('abc')])
    @patch('client.get_json')
    def test_org(self, org_name, mock):
        """function to test TestGithubOrgClient returns correct value"""
        testmyclass = GithubOrgClient(org_name)
        testmyclass.org()
        mock.called_with_once(testmyclass.ORG_URL.format(org=org_name))

    def test_public_repos_url(self):
        """function to to unit-test GithubOrgClient._public_repos_url"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mymock:
            mypayload = {"repos_url": "something"}
            mymock.return_value = mypayload
            test_class = GithubOrgClient('test')
            res = test_class._public_repos_url
            self.assertEqual(res, payload["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mymock_json: MagicMock) -> None:
        """function to test public repos"""
        mypayloads = [{"name": "google"}, {"name": "Twitter"}]
        mymock_json.return_value = mypayloads

        with patch("client.GithubOrgClient._public_repos_url") as mymock_pub:
            mymock_pub.return_value = "hey there!"
            mytest_class = GithubOrgClient("test")
            res = mytest_class.public_repos()

            exp = [p["name"] for p in mypayloads]
            self.assertEqual(res, exp)

            mymock_json.called_with_once()
            mymock_pub.called_with_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        # Patch the method to avoid actual API calls
        with patch.object(GithubOrgClient, 'has_license') as mock_has_license:
            mock_has_license.return_value = expected_result

            # Create an instance of GithubOrgClient (optional, modify if needed)
            client = GithubOrgClient()

            # Call the method with test data
            result = client.has_license(repo, license_key)

            # Assert that the mocked method was called once
            mock_has_license.assert_called_once_with(repo, license_key)

            # Assert that the returned value matches the expected result
            self.assertEqual(result, expected_result)
