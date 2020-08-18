# json-filter

Filters the information from complicated json output to a more sweet view to us humans. Personally, I used much for filter AWS CLI output long json strings in the output.

This program can help to work with any other program that outputs some json (or even json files).

## Installing
Navigates to the project root, then type:
```
pip install .
```

## Usage

Just redirects any json content to `jfilter` command line:

```
some_program_that_outputs_json | jfilter your.json.navigation
```

### Example

Json output sample:

```json
{
    "SecurityGroups": [
        {
            "Description": "Access to database from santa fe",
            "GroupName": "santa-fe-mysql"
        },
        {
            "Description": "SSH access from any other place",
            "GroupName": "Ssh outside"
        },
        {
            "Description": "This was given by AWS",
            "GroupName": "awseb-e-dfasfasd-stack-AWSEBSecurityGroup-ASDFDFAASDF"
        }
    ]
}
```

Type:
```
cat contents.json | jfilter SecurityGroups.2.GroupName
```

Then, you got:
```
awseb-e-dfasfasd-stack-AWSEBSecurityGroup-ASDFDFAASDF
```

You may want get a simple field from a longer list:
```
cat contents.json | jfilter SecurityGroups..GroupName
```

Then, the response:
```
* santa-fe-mysql
* Ssh outside
* awseb-e-dfasfasd-stack-AWSEBSecurityGroup-ASDFDFAASDF
```
