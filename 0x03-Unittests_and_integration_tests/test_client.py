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
