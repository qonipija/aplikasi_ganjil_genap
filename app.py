import streamlit as st

st.header('Define Number Type Apps', divider='violet')
st.write('Ini adalah aplikasi untuk menentukan bilangan genap atau ganjil')

# Input angka pertama dan kedua
number1 = st.number_input('Masukkan angka pertama')
number2 = st.number_input('Masukkan angka kedua')

# Determine if number1 is even or odd
if number1 % 2 == 0:
    number1_type = 'genap'
else:
    number1_type = 'ganjil'

# Determine if number2 is even or odd
if number2 % 2 == 0:
    number2_type = 'genap'
else:
    number2_type = 'ganjil'

# Calculate the product
product = number1 * number2

# Determine if product is even or odd
if product % 2 == 0:
    product_type = 'genap'
else:
    product_type = 'ganjil'

# Display results
st.markdown("---")  # Divider line in violet color
st.write(f'Angka {number1} adalah bilangan {number1_type}.')
st.write(f'Angka {number2} adalah bilangan {number2_type}.')
st.write(f'Hasil perkalian {number1} dan {number2} adalah {product}.')
st.write(f'Hasil perkalian {number1} dan {number2} adalah bilangan {product_type}.')