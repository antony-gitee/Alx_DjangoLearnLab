<!-- example: bookshelf/templates/bookshelf/form_example.html -->
<form method="POST" action="{% url 'create_book' %}">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>

