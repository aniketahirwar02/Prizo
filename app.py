from flask import Flask, render_template, request
from products import products

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about_page')
def about_page():
    return render_template('about_page.html')


@app.route('/contact_page')
def contact_page():
    return render_template('contact_page.html')


@app.route('/search')
def search():

    query = request.args.get('q')

    filtered_products = []

    for product in products:
        if query.lower() in product['name'].lower():
            filtered_products.append(product)

    return render_template(
        'result_page.html',
        products=filtered_products,
        query=query
    )


@app.route('/comparison_page/<int:product_id>')
def comparison_page(product_id):

    selected_product = None

    for product in products:
        if product['id'] == product_id:
            selected_product = product
            break

    comparison_products = []

    for product in products:
        if product['name'] == selected_product['name']:
            comparison_products.append(product)

    best_price = min(comparison_products, key=lambda x: x['price'])

    return render_template(
        'comparison_page.html',
        product=selected_product,
        comparison_products=comparison_products,
        best_price=best_price
    )


if __name__ == '__main__':
    app.run(debug=True)