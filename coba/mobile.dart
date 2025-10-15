import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(title: 'Login & Shopping Cart', home: LoginPage());
  }
}

class LoginPage extends StatefulWidget {
  @override
  _LoginPageState createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final _formKey = GlobalKey<FormState>();
  String _username = '';
  String _password = '';

  void _login() {
    if (_formKey.currentState!.validate()) {
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(builder: (context) => ShoppingCartPage()),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Login')),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Form(
          key: _formKey,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              TextFormField(
                decoration: InputDecoration(labelText: 'Username'),
                onChanged: (val) => _username = val,
                validator: (val) => val!.isEmpty ? 'Enter username' : null,
              ),
              TextFormField(
                decoration: InputDecoration(labelText: 'Password'),
                obscureText: true,
                onChanged: (val) => _password = val,
                validator: (val) => val!.isEmpty ? 'Enter password' : null,
              ),
              SizedBox(height: 20),
              ElevatedButton(onPressed: _login, child: Text('Login')),
            ],
          ),
        ),
      ),
    );
  }
}

class ShoppingCartPage extends StatelessWidget {
  final List<Map<String, dynamic>> items = [
    {'name': 'Apple', 'price': 2},
    {'name': 'Banana', 'price': 1},
    {'name': 'Orange', 'price': 3},
  ];

  @override
  Widget build(BuildContext context) {
    int total = items.fold(0, (sum, item) => sum + item['price'] as int);

    return Scaffold(
      appBar: AppBar(title: Text('Shopping Cart')),
      body: ListView(
        children: [
          ...items.map(
            (item) => ListTile(
              title: Text(item['name']),
              trailing: Text('\$${item['price']}'),
            ),
          ),
          Divider(),
          ListTile(title: Text('Total'), trailing: Text('\$$total')),
        ],
      ),
    );
  }
}
