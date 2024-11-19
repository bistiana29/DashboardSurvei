import pandas as pd
import streamlit as st
from PIL import Image
import altair as alt
import plotly.express as px
from plotly.subplots import make_subplots
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
import matplotlib.pyplot as plt

df = pd.read_excel('df_sampledfix.xlsx')

im = Image.open('Logo_PENS.png')
st.set_page_config(page_title="dashboardKenapaPENS?", layout="wide", page_icon=im)

logo = Image.open("Logo_PENS.png")

col1, col2 = st.columns([1, 6])
with col1:
    st.image(logo, width=85)
with col2:
    st.markdown(
    """ <div> <h1 style='font-size: 35px; margin: 0;'><center>Dashboard Survei Alasan Mahasiswa Memilih PENS</center></h1> </div> """,
    unsafe_allow_html=True )

with st.sidebar:
    choose = option_menu(
        "Dashboard menu", 
        ["Dataset", "Overview", "Page 1", "Page 2", "Page 3"], 
        icons=['database', 'house', "bar-chart", "bar-chart", "bar-chart"],
        menu_icon="cast",
        default_index=1,  
    )

# Dataset
if choose == "Dataset":
    st.subheader('Dataset Sampel Survei🗃️:')
    st.write(df)

# Overview
elif choose == "Overview":
    col1a, col2a, col3a, col4a = st.columns([2, 2, 2, 2])
    
    box_style = """
        <style>
        .box {
            padding: 10px;
            border: 2px solid #FFEB00;
            border-radius: 5px;
            font-weight: bold;
            font-size: 34px;
            text-align: center;
        }
        .center-subheader {
            text-align: center;
            font-weight: bold;
            font-size: 18px;
            margin-top: 10px;
            margin-bottom: 5px;
        }
        </style>
    """
    st.markdown(box_style, unsafe_allow_html=True)

    with col1a:
        st.markdown('<div class="center-subheader">Sampel</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="box">{df["Nama"].count()}</div>', unsafe_allow_html=True)
    
    with col2a:
        st.markdown('<div class="center-subheader">Program Studi</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="box">{df["Prodi"].nunique()}</div>', unsafe_allow_html=True)
    
    with col3a:
        st.markdown('<div class="center-subheader">Departemen</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="box">{df["Departemen"].nunique()}</div>', unsafe_allow_html=True)
    
    with col4a:
        st.markdown('<div class="center-subheader">Angkatan</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="box">{df["Angkatan"].nunique()}</div>', unsafe_allow_html=True)
    
    col1b, col2b, col3b = st.columns([3, 3, 5])
    box_style = """
        <style>
        .center-subheader {
            text-align: center;
            font-weight: bold;
            font-size: 18px;
            margin-top: 10px;
            margin-bottom: 5px;
        }
        </style>
    """
    st.markdown(box_style, unsafe_allow_html=True)

    with col1b:
        st.markdown('<div class="center-subheader">Asal Daerah</div>', unsafe_allow_html=True)
        frekuensi = df['Asal Daerah'].value_counts().reset_index()
        frekuensi.columns = ['Asal', 'Frekuensi']
        
        fig = px.pie(frekuensi, names='Asal', values='Frekuensi')
        fig.update_layout(legend_title_text='Asal Daerah', legend=dict(x=1, y=1))
        st.plotly_chart(fig)
    
    with col2b:
        st.markdown('<div class="center-subheader">Jenjang Pendidikan Sebelumnya</div>', unsafe_allow_html=True)
        frekuensi = df['Jenjang Pendidikan Sebelumnya'].value_counts().reset_index()
        frekuensi.columns = ['Pendidikan Sebelumnya', 'Frekuensi']

        fig = px.pie(frekuensi, names='Pendidikan Sebelumnya', values='Frekuensi',
                    hole=0.6)
        fig.update_layout(legend_title_text='Pendidikan Sebelumnya', legend=dict(x=1, y=1))
        st.plotly_chart(fig)
    
    with col3b:
        st.markdown('<div class="center-subheader">Boxplot Total Skor</div>', unsafe_allow_html=True)
        fig = px.box(df, x='Departemen', y='Total Skor',
                    labels={"Total Skor": "Total Skor", "Departemen": "Departemen"},
                    color="Departemen")

        fig.update_layout(
            xaxis=dict(title='', showticklabels=False),
            yaxis=dict(title=''),
        )
        st.plotly_chart(fig, use_container_width=True)

# Page 1
elif choose == "Page 1":
    col1c, col2c, col3c = st.columns([5,5,4])
    box_style = """
        <style>
        .center-subheader {
            text-align: center;
            font-weight: bold;
            font-size: 18px;
            margin-top: 10px;
            margin-bottom: 5px;
        }
        </style>
    """
    st.markdown(box_style, unsafe_allow_html=True)
    with col1c:
        st.markdown('<div class="center-subheader">Pengaruh Jalur masuk</div>', unsafe_allow_html=True)
        frekuensi = df['Apakah jalur masuk berpengaruh terhadap keputusan Anda dalam memilih PENS?'].value_counts().reset_index()
        frekuensi.columns = ['Skala', 'Frekuensi']
        fig = px.bar(frekuensi, x='Frekuensi', y='Skala',
            labels={'Skala': 'Skala', 'Frekuensi': 'Frekuensi Responden'},
            color='Skala',
            orientation='h')
        fig.update_layout(
            height=300,
            width=500 
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2c:
        st.markdown('<div class="center-subheader">Jalur masuk</div>', unsafe_allow_html=True)
        frekuensi = df['Melalui jalur apa Anda diterima di PENS? '].value_counts().reset_index()
        frekuensi.columns = ['Jalur', 'Frekuensi']
        frekuensi = frekuensi.sort_values(by='Frekuensi', ascending=False)
        fig = px.bar(frekuensi, x='Frekuensi', y='Jalur', color="Jalur", orientation='h')
        fig.update_layout(
            height=300,
            width=500,
            yaxis=dict(title='Jalur', showticklabels=False),
            xaxis=dict(title='Frekuensi'),
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    with col3c:
        st.markdown('<div class="center-subheader">Prioritas Pilihan</div>', unsafe_allow_html=True)
        frekuensi = df['Saat Anda memilih program studi di PENS, pada pilihan ke berapakah program studi yang Anda jalani saat ini?'].value_counts().reset_index()
        frekuensi.columns = ['Pilihan', 'Frekuensi']
        fig = px.pie(frekuensi, names='Pilihan', values='Frekuensi',
                    hole=0.6)
        fig.update_layout(legend_title_text='Pilihan Program Studi', legend=dict(x=1, y=1),
        height=300, width=500)
        st.plotly_chart(fig, use_container_width=True)
    
    col1d, col2d = st.columns([5, 4])
    box_style = """
        <style>
        .center-subheader {
            text-align: center;
            font-weight: bold;
            font-size: 18px;
            margin-top: 10px;
            margin-bottom: 5px;
        }
        </style>
    """
    st.markdown(box_style, unsafe_allow_html=True)
    with col1d:
        st.markdown('<div class="center-subheader">Sumber Informasi</div>', unsafe_allow_html=True)
        df_sumber = df['Dari mana Anda mengetahui informasi tentang PENS?'].str.split(',', expand=True)
        df_sumber.columns = ['Website', 'Social_Media', 'Poster/Spanduk/Brosur', 'Keluarga/Kerabat', 'Teman/Kakak Kelas', 'Alumni', 'Guru']
        df_sumber = df_sumber.apply(lambda x: x.str.strip()).stack().value_counts()
        df_sumber = df_sumber.reset_index()
        df_sumber.columns = ['Sumber Informasi', 'Frekuensi'] 
        fig = px.treemap(
            df_sumber,
            path=["Sumber Informasi"],
            hover_data={'Sumber Informasi': True, 'Frekuensi': True},
            values="Frekuensi",
        )
        st.plotly_chart(fig)
    
    with col2d:
        st.markdown('<div class="center-subheader">Sosial Media</div>', unsafe_allow_html=True)
        df_sosmed = df['Jika dari Sosial Media PENS, pada platform apa kalian mengetahui informasi tentang PENS?'].str.split(r'[-,]', expand=True)
        df_sosmed = df_sosmed.apply(lambda x: x.str.strip())
        df_sosmed = df_sosmed.stack().value_counts()
        df_sosmed = df_sosmed.reset_index()
        df_sosmed.columns = ['Sosial Media', 'Frekuensi']
        fig = px.pie(df_sosmed, names='Sosial Media', values='Frekuensi')
        fig.update_layout(legend_title_text='Sosial Media', legend=dict(x=1, y=1),
        margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig, use_container_width=True)

# Page 2
elif choose == "Page 2":
    col1c, col2c, col3c = st.columns([4,5,5])
    box_style = """
        <style>
        .center-subheader {
            text-align: center;
            font-weight: bold;
            font-size: 18px;
            margin-top: 10px;
            margin-bottom: 5px;
        }
        </style>
    """
    st.markdown(box_style, unsafe_allow_html=True)
    with col1c:
        st.markdown('<div class="center-subheader">Rasa Penasaran</div>', unsafe_allow_html=True)
        frekuensi = df['Apakah Anda mencari Informasi mengenai akreditasi program studi sebelum memutuskan untuk mendaftar di kampus PENS'].value_counts().reset_index(False)
        frekuensi.columns = ['Keputusan', 'Frekuensi']
        fig = px.pie(frekuensi, names='Keputusan', values='Frekuensi')
        fig.update_layout(legend_title_text='Keputusan', legend=dict(x=1, y=1),
        height=300,
        width=500)
        st.plotly_chart(fig, use_container_width=True)

    with col2c:
        st.markdown('<div class="center-subheader">Peringkat Kampus Vs Akreditasi Program Studi</div>', unsafe_allow_html=True)
        frekuensi1 = df['Seberapa penting peringkat kampus dalam memengaruhi keputusan Anda dalam memilih PENS?'].value_counts()
        frekuensi2 = df['Seberapa penting akreditasi program studi dalam keputusan Anda memilih PENS?'].value_counts()
        data = pd.DataFrame({
            'Skala': frekuensi1.index.tolist() + frekuensi2.index.tolist(),
            'Frekuensi': list(frekuensi1.values) + list(frekuensi2.values),
            'Penilaian': ['Peringkat Kampus'] * len(frekuensi1) + ['Akreditasi Program Studi'] * len(frekuensi2)
        })
        fig = px.bar(
            data, x='Skala', y='Frekuensi', color='Penilaian', barmode='group',
            labels={'Skala': 'Skala', 'Frekuensi': 'Frekuensi'}, height=300, width=500
        )
        st.plotly_chart(fig)

    with col3c:
        st.markdown('<div class="center-subheader">Fasilitas Akademik Vs Fasilitas Non-Akademik</div>', unsafe_allow_html=True)
        frekuensi1 = df['Apakah fasilitas penunjang akademik seperti kelas, laboratorium, perpustakaan, dan auditorium memengaruhi keputusan Anda dalam memilih kampus ini? '].value_counts()
        frekuensi2 = df['Apakah fasilitas penunjang non-akademik seperti masjid, kantin, lapangan, parkiran, dan kamar mandi memengaruhi keputusan Anda dalam memilih kampus ini?'].value_counts()
        data = pd.DataFrame({
            'Skala': frekuensi1.index.tolist() + frekuensi2.index.tolist(),
            'Frekuensi': list(frekuensi1.values) + list(frekuensi2.values),
            'Fasilitas': ['Akademik'] * len(frekuensi1) + ['Non-Akademik'] * len(frekuensi2)
        })
        fig = px.bar(
            data, x='Skala', y='Frekuensi', color='Fasilitas', barmode='group',
            labels={'Skala': 'Skala', 'Frekuensi': 'Frekuensi'}, height=300, width=500
        )
        st.plotly_chart(fig)
    
    col1d, col2d = st.columns([5,5])
    box_style = """
        <style>
        .center-subheader {
            text-align: center;
            font-weight: bold;
            font-size: 18px;
            margin-top: 10px;
            margin-bottom: 5px;
        }
        </style>
    """
    st.markdown(box_style, unsafe_allow_html=True)
    with col1d:
        st.markdown('<div class="center-subheader">Jarak Kampus</div>', unsafe_allow_html=True)
        frekuensi = df['Apakah jarak kampus PENS dari rumah atau tempat tinggal memengaruhi keputusan Anda?'].value_counts().reset_index()
        frekuensi.columns = ['Skala', 'Frekuensi']
        fig = px.bar(frekuensi, x='Frekuensi', y='Skala',
            labels={'Skala': 'Skala', 'Frekuensi': 'Frekuensi'},
            color='Skala',
            orientation='h')
        fig.update_layout(
            height=300,
            width=500 
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2d:
        st.markdown('<div class="center-subheader">Lokasi Kampus</div>', unsafe_allow_html=True)
        frekuensi = df['Seberapa penting lokasi kampus PENS dalam mempengaruhi keputusan Anda?'].value_counts().reset_index()
        frekuensi.columns = ['Skala', 'Frekuensi']
        fig = px.bar(frekuensi, x='Frekuensi', y='Skala',
            labels={'Skala': 'Skala', 'Frekuensi': 'Frekuensi'},
            color='Skala',
            orientation='h')
        fig.update_layout(
            height=300,
            width=500 
        )
        st.plotly_chart(fig, use_container_width=True)

# Page 3
elif choose == "Page 3":
    col1c, col2c, col3c = st.columns([4,5,5])
    box_style = """
        <style>
        .center-subheader {
            text-align: center;
            font-weight: bold;
            font-size: 18px;
            margin-top: 10px;
            margin-bottom: 5px;
        }
        </style>
    """
    st.markdown(box_style, unsafe_allow_html=True)
    with col1c:
        st.markdown('<div class="center-subheader">Beasiswa Vs Non-Beasiswa</div>', unsafe_allow_html=True)
        frekuensi = df['Apakah saat ini Anda sedang menerima beasiswa?'].value_counts().reset_index(False)
        frekuensi.columns = ['Status', 'Frekuensi']
        fig = px.pie(frekuensi, names='Status', values='Frekuensi')
        fig.update_layout(legend_title_text='Status', legend=dict(x=1, y=1),
        height=300,
        width=500)
        st.plotly_chart(fig, use_container_width=True)

    with col2c:
        st.markdown('<div class="center-subheader">Pengaruh Ketersediaan Beasiswa</div>', unsafe_allow_html=True)
        frekuensi = df['Apakah beasiswa atau bantuan keuangan memengaruhi keputusan anda saat memilih PENS?'].value_counts().reset_index()
        frekuensi.columns = ['Skala', 'Frekuensi']
        fig = px.bar(frekuensi, x='Frekuensi', y='Skala',
            labels={'Skala': 'Skala', 'Frekuensi': 'Frekuensi'},
            color='Skala',
            orientation='h')
        fig.update_layout(
            height=300,
            width=500 
        )
        st.plotly_chart(fig, use_container_width=True)

    with col3c:
        st.markdown('<div class="center-subheader">Penilaian Biaya Pendidikan</div>', unsafe_allow_html=True)
        frekuensi = df['Bagaimana Anda menilai biaya pendidikan di PENS dibandingkan dengan institusi lain?'].value_counts().reset_index()
        frekuensi.columns = ['Skala', 'Frekuensi']
        fig = px.bar(frekuensi, x='Frekuensi', y='Skala',
            labels={'Skala': 'Skala', 'Frekuensi': 'Frekuensi'},
            color='Skala',
            orientation='h')
        fig.update_layout(
            height=300,
            width=500 
        )
        st.plotly_chart(fig, use_container_width=True)
    
    col1d, col2d = st.columns([5, 5])
    box_style = """
        <style>
        .center-subheader {
            text-align: center;
            font-weight: bold;
            font-size: 18px;
            margin-top: 10px;
            margin-bottom: 5px;
        }
        </style>
    """
    st.markdown(box_style, unsafe_allow_html=True)
    with col1d:
        st.markdown('<div class="center-subheader">Pengaruh Jaringan Alumni</div>', unsafe_allow_html=True)
        frekuensi = df['Seberapa penting jaringan alumni PENS dalam keputusan Anda?'].value_counts().reset_index()
        frekuensi.columns = ['Skala', 'Frekuensi']
        fig = px.bar(frekuensi, x='Skala', y='Frekuensi',
            labels={'Skala': 'Skala', 'Frekuensi': 'Frekuensi'},
            color='Skala')
        fig.update_layout(
            height=300,
            width=500 
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2d:
        st.markdown('<div class="center-subheader">Sebaran Kluster</div>', unsafe_allow_html=True)
        df['Cluster'] = df['Cluster'].astype(str)
        fig = px.scatter(df, x='PCA 1', y='PCA 2',
                color='Cluster',
                color_discrete_map={ '0': '#FA4032', '1': '#3D3BF3', '2': 'lightgreen'},
                labels={"X": "X Axis", "Y": "Y Axis"},
                hover_data=['Cluster', 'Departemen'])
        fig.update_layout(
            height=350,
            width=500 
        )
        st.plotly_chart(fig, use_container_width=True)