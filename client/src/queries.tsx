const host = 'http://127.0.0.1:5000/';
export const SEARCH = (type: string) => `${host}/query/${type}`;
export const CDN = (filename: string) => `${host}/cdn/${filename}`;
export const INC = (id: number, type: string) => `${host}/inc/${id}/${type}`;

export const types = [
    'shirt',
    'top',
    'sweater',
    'cardigan',
    'jacket',
    'vest',
    'pants',
    'shorts',
    'skirt',
    'coat',
    'dress',
    'jumpsuit',
    'cape',
    'glasses',
    'hat',
    'headband',
    'tie',
    'glove',
    'watch',
    'belt',
    'sock',
    'shoe',
    'bag',
    'scarf',
    'hood'
]