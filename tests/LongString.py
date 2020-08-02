class LongString:

    def get_string(self) -> str:
        return '''{
        "SecurityGroups": [
            {
                "Description": "santa-fe-mysql",
                "GroupName": "santa-fe-mysql",
                "IpPermissions": [],
                "OwnerId": "12384716293876",
                "GroupId": "sg-abc123ab12",
                "IpPermissionsEgress": [
                    {
                        "IpProtocol": "-1",
                        "IpRanges": [
                            {
                                "CidrIp": "0.0.0.0/0"
                            }
                        ],
                        "Ipv6Ranges": [],
                        "PrefixListIds": [],
                        "UserIdGroupPairs": []
                    }
                ],
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": "Santa Fé mysql"
                    }
                ],
                "VpcId": "vpc-12zbcd21"
            },
            {
                "Description": "Ssh from outside",
                "GroupName": "Ssh outside",
                "IpPermissions": [
                    {
                        "FromPort": 22,
                        "IpProtocol": "tcp",
                        "IpRanges": [
                            {
                                "CidrIp": "123.32.123.32/32"
                            }
                        ],
                        "Ipv6Ranges": [],
                        "PrefixListIds": [],
                        "ToPort": 22,
                        "UserIdGroupPairs": []
                    }
                ],
                "OwnerId": "12384716293876",
                "GroupId": "sg-12ab1a2b",
                "IpPermissionsEgress": [
                    {
                        "IpProtocol": "-1",
                        "IpRanges": [
                            {
                                "CidrIp": "0.0.0.0/0"
                            }
                        ],
                        "Ipv6Ranges": [],
                        "PrefixListIds": [],
                        "UserIdGroupPairs": []
                    }
                ],
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": "Ssh from outside"
                    }
                ],
                "VpcId": "vpc-1212abc"
            },
            {
                "Description": "SecurityGroup for ElasticBeanstalk environment",
                "GroupName": "awseb-e-dfasfasd-stack-AWSEBSecurityGroup-ASDFDFAASDF",
                "IpPermissions": [
                    {
                        "FromPort": 80,
                        "IpProtocol": "tcp",
                        "IpRanges": [],
                        "Ipv6Ranges": [],
                        "PrefixListIds": [],
                        "ToPort": 80,
                        "UserIdGroupPairs": [
                            {
                                "GroupId": "sg-abc123890ab",
                                "UserId": "12384716293876"
                            }
                        ]
                    },
                    {
                        "FromPort": 22,
                        "IpProtocol": "tcp",
                        "IpRanges": [
                            {
                                "CidrIp": "0.0.0.0/0"
                            }
                        ],
                        "Ipv6Ranges": [],
                        "PrefixListIds": [],
                        "ToPort": 22,
                        "UserIdGroupPairs": []
                    }
                ],
                "OwnerId": "12384716293876",
                "GroupId": "sg-ababc123890abf",
                "IpPermissionsEgress": [
                    {
                        "IpProtocol": "-1",
                        "IpRanges": [
                            {
                                "CidrIp": "0.0.0.0/0"
                            }
                        ],
                        "Ipv6Ranges": [],
                        "PrefixListIds": [],
                        "UserIdGroupPairs": []
                    }
                ],
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": "my-env"
                    },
                    {
                        "Key": "elasticbeanstalk:environment-id",
                        "Value": "e-akjfgakjsdg"
                    },
                    {
                        "Key": "elasticbeanstalk:environment-name",
                        "Value": "my-env"
                    },
                    {
                        "Key": "aws:cloudformation:stack-name",
                        "Value": "awseb-e-akjfgakjsdg-stack"
                    },
                    {
                        "Key": "aws:cloudformation:logical-id",
                        "Value": "AWSEBSecurityGroup"
                    },
                    {
                        "Key": "aws:cloudformation:stack-id",
                        "Value": "arn:aws:cloudformation:ak-norwest-1:12384716293876:stack/awseb-e-akjfgakjsdg-stack/ab123"
                    }
                ],
                "VpcId": "vpc-0923abcf"
            }
        ]
    }
    '''
