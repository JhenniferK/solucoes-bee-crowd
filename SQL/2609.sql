select categories.name, sum(products.amount)
from categories, products
where categories.id = products.id_categories
group by categories.name;
