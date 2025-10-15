from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def page_home(request):
    return Response('Hello World!')


def page_test(request):
    nama=request.matchdict['nama']
    return Response(f'Ini halaman test, nama: {nama}')

def hitung_usia(lahir):
    """Menghitung usia dari tanggal lahir dalam format dd-mm-yyyy

    Args:
        lahir (str): Tanggal lahir dalam format dd-mm-yyyy

    Returns:
        int tahun: Usia dalam tahun
        int hari: Kelebihan hari setelah ulang tahun terakhir
    Logics:
        1. Tahun = tahun sekarang - tahun lahir
        2. Jika bulan sekarang < bulan lahir, tahun -= 1
        3. Jika bulan sekarang == bulan lahir dan tgl sekarang < tgl lahir, tahun -= 1
        4. hari = tgl sekarang - tgl ulang tahun terakhir
        
    """
    from datetime import datetime, date
    tanggal_lahir = datetime.strptime(lahir, '%d-%m-%Y')
    sekarang = datetime.now()
    tahun = sekarang.year - tanggal_lahir.year
    hari = 0
    if (sekarang.month, sekarang.day) < (tanggal_lahir.month, tanggal_lahir.day):
        tahun -= 1
    if (sekarang.month, sekarang.day) > (tanggal_lahir.month, tanggal_lahir.day):
        hari = sekarang.date() - date(sekarang.year, tanggal_lahir.month, tanggal_lahir.day)
    return tahun, hari  # Mengembalikan usia dalam tahun

def page_uji(request):
    nama=request.params.get('nama', 'Tidak ada nama')
    alamat = request.params.get('alamat', 'Tidak ada alamat')
    lahir = request.params.get('lahir', 'Tidak ada tanggal lahir')
    # Berapa usaia sampai detik ini?

    return Response(f"""Ini halaman uji, nama: {nama},<br>
                     alamat: {alamat}, <br>
                     tanggal lahir: {lahir}<br>
                     usia: {hitung_usia(lahir)} tahun""")

def page_coba(request):
    return Response('Ini halaman coba')

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('home', '/')
        config.add_route('test', '/test/{nama}')
        config.add_route('uji', '/uji')
        config.add_route('coba', '/coba')

        config.add_view(page_home, route_name='home')
        config.add_view(page_test, route_name='test')
        config.add_view(page_uji, route_name='uji')
        config.add_view(page_coba, route_name='coba')
        
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
