# googletrans client-server program

## Technology
- python 3.8
- googletrans 4.0.0rc1


A server that receives text and retreives translated text and returns to client.

# How to 
- __NEED active Internet Connection__
- Using `pipenv` create a virtualenv
- from inside run `myTranslator.py` to start the `server`
- from inside run `clienEnd.py` to start a `client`.
- in `clientEnd.py` type any text and press enter to receive the translated text in `bangla` by default.Depending on the font language might look broken. 
- to change the translated language, type `set_dest:ja` for `japanese`
- for all `set_dest:` keys check [API Documentation of googletrans](https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages)
- after setting up the destination you will receive all following text translated to that language.
- restarting the application resets the `set_dest:` to `bn` i.e. bangla  
