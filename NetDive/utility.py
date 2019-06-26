def get_dummy_api_key():
    dummy_key = str()
    for i in range(4):
        r = base64.b64encode(uuid.uuid4().bytes).decode('utf-8').lower()
        dummy_key += r
    dummy_key = ''.join([c for c in dummy_key if c.isalnum()])
    dummy_key = dummy_key[:63]
    return dummy_key

def populate_settings(sfile):
    # Populate dictionary with your stored settings
    sett = {}
    with open(sfile, 'r') as keys:
        for key in keys:
            k, v = key.split(': ')
            if v.endswith('\n'): v = v[:-1]
            sett[k] = v
    keys.close()
    return sett

def load_apikeys():
    API_KEYS = populate_settings('./settings/api_keys.txt')
    ipdata_api = { 'api-key': API_KEYS['ipdata'] }
    print('IPData API key successfully loaded')
    
    vt_api = { 'apikey': API_KEYS['VirusTotal'] }
    vt = VTAPI(vt_api['apikey'])
    print('VirusTotal API key successfully loaded')
    
    wdsi_api = { 'api-key': API_KEYS['WDSI'] }
    print('WDSI API key successfully loaded')

    return ipdata_api, vt_api, vt, wdsi_api

def load_ip_list():
    q = []
    q_ports = {}
    fname = 'ips.txt'
    with open('./search_blobs/{}'.format(fname), 'r') as f:
        rec = csv.reader(f)
        for r in rec:
            try:
                i, p = r[0].split(':')
            except:
                i = r[0]
                p = 443
            q.append(i)     # ip addresses
            q_ports[i] = {
                'host': '',
                'port': p
            }
    f.close()
    return q, q_ports

def load_hostname_list():
    q = {}
    fname = 'hostnames.txt'
    with open('./search_blobs/{}'.format(fname), 'r') as f:
        rec = csv.reader(f)
        for r in rec:
            q[r[0]] = {}
    f.close()
    return q

def combine_rows(df, grpby, comb_col):
    df = df.groupby(grpby)[comb_col].apply(set).reset_index()
    return df

def df_to_csv(out, file):
    with open(file, 'w', newline='', encoding='utf-8') as f:
        out.to_csv(path_or_buf=f)
    clear_output(wait=True)
    print('Saved Output to {}'.format(file))

def split_list(lst, key):
    dic = {}
    for i, e in enumerate(lst):
        k = '{}{}'.format(key, i + 1)
        dic[k] = e
    return dic

def decode_bytes(data):
    data = { key.decode(): val.decode() for key, val in data.items() }
    return data

def dict_to_dataframe(_dict, column):
    unzip = pd.concat(
        [_dict.drop([column], axis=1), 
        _dict[column].apply(pd.Series)], 
        axis=1).fillna('None')
    return unzip