def test_GetImpact360Token():

    authToken = getImpact360AuthToken(os.environ['HOST'], isSSL,ValueStorage.Tenant_A_Admin, getPassword(ValueStorage.Tenant_A_Admin))
    print ( f"Impact360 Token = {authToken}")



def getImpact360AuthToken(host, isSSL, username, password):
    global authToken

    if (isSSL is None or isSSL == False):
        protocol = 'http://'
    else:
        protocol = 'https://'

    # create an authentication request
    authRequest = requests.Session()

    # Authorization using username/password
    authRequest.headers.update({'Content-Type': 'application/json'})
    authJson = {"user": username, "password": password}
    authURL = f'{protocol}{host}/wfo/rest/core-api/auth/token'

    try:
        authResponse = authRequest.post(authURL, json=authJson, verify=True)
    except Exception as err:
        print(f"Not able to connect to {host} using {authJson} - Unexpected {err=}, {type(err)=}")
        raise

    if (authResponse.status_code != OK):
        raise ValueError(f'Not able to connect to {host} using {authJson} -Error: {authResponse.status_code}')
    else:
        # Get authentication token
        authToken = json.loads(authResponse.text)['AuthToken']['token']
        return authToken