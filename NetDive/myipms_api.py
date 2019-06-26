import deps
import utility as u

'''
-------------------------------------------------------------------------------
Project:        MyIP.ms API in Python
Author:         Whitney King (@WhitneyOnTheWeb)
File:           myipsms_api.py

This project is intended to translate the RESTful APIs provided on the MyIP.ms
website into a usable Python utility for investigating details and connections
between different entities on the internet.

-------------------------------------------------------------------------------
Resources:      https://myip.ms/info/api/API_Dashboard.html

Variable	    Value
--------        -----
api_id	        Unique for logged in user
api_key	        Unique for logged in user
api_url	        Unique for logged in user

query	        ... any IP Address or Website Name ....
    Example:        yahoo.com, webstore.illinois.edu, 12.12.12.100, etc.

timestamp:  	GMT current timestamp in format gmdate("Y-m-d_H:i:s")
    Example:        2019-06-24_01:14:45

signature:	    MD5 hash --> JSON
    Syntax:
    -------
        md5(
            $api_url/$query/api_id/$api_id/api_key/$api_key/
            timestamp/$timestamp
        )

URL/IP:           Host --> JSON
    Syntax:
    -------
    $api_url/$query/api_id/$api_id/api_key/$api_key/
    signature/$signature/timestamp/$timestamp

        *Enable Array Output: add '/asarray/yes' to the end of the syntax

-------------------------------------------------------------------------------
Logs:
-----
* 24-06-2019 (v1.0):  Project creation and initial design of concept


-------------------------------------------------------------------------------

'''