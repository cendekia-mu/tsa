# Hari ke 10

## Tujuan: Menghubungkan Pyramid dengan HTML/template
1. Install chameleon
  
   ```pip install pyramid_chameleon```
   
2. Include (menyertakan) Chameleon kedalam config di main module
   
   ```config.include("pyramid_chameleon")```
3. Membuat template yang berakhiran ```.pt```
4. Menghubungkan view dengan template dengan parameter ```renderer```

```@view_config(route_name='home', renderer='templates/home.pt')```

5. Mengirim variable dari ```view``` ke template
   a. Nilai Pengembalian ```return``` dalan view:

   ```return {"nama_variable": isi_variable}```

   b. Dalam template gunakan cara beruikut untuk menampilkan variabel:

   ```${nama_variabel}```

# Static Asset    
1. Image
2. Style (.css)
3. JavaScript (.js)

## Langkah2
1. Membuat folder berisi static asset
2. Menyertakan folder kedalam aplikasi
   
   ```config.add_static_view(name="static_name", path="static_location_file")```
3. Memanggil file dalam static asset

# Outputing JSON

```@view_config(route_name='home.json', renderer='json')```

