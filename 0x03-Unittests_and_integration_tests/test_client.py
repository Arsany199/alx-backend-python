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
    def test_has_license(self, repo: Dict, key: str, expected: bool):
        """function tests the license method"""
        res = GithubOrgClient("google")
        client_licence = res.has_license(repo, key)
        self.assertEqual(client_licence, expected)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """define testintegrationgithuborgclient class"""
    @classmethod
    def setUpClass(cls):
        """function that run set up before test"""
        conf = {"return_value.json.side_effect": [
            cls.org_payload, cls.repos_payload,
            cls.org_payload, cls.repos_payload
        ]}

        cls.get_patcher = patch('requests.get', **conf)
        cls.mock = cls.get_patcher.start()

    def test_public_repo(self):
        """function that integration test public repo"""
        mytest_class = GithubOrgClient('Google')

        self.assertEqual(mytest_class.org, self.org_payload)
        self.assertEqual(mytest_class.repos_payload, self.repos_payload)
        self.assertEqual(mytest_class.public_repos(), self.expected_repos)
        self.assertEqual(mytest_class.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """function integration test repos with License"""
        mytest_class = GithubOrgClient("google")

        self.assertEqual(mytest_class.public_repos(), self.expected_repos)
        self.assertEqual(mytest_class.public_repos("XLICENSE"), [])
        self.assertEqual(mytest_class.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """function that run after test"""
        cls.get_patcher.stop()
