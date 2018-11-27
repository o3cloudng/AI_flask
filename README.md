# tensorflask
This is a simple example of hosting a TensorFlow model as Flask service for inference. It provides the "Poodle, Pug or Weiner Dog?" image identification service using a retrained MobileNet model. The retrained model/labels are provided here to let you run the service locally.


## Usage
Once you've started the service, you can query it on `localhost:8000`. You can either hit it via a web browser, or use `curl` from the commandline. It takes a single parameter `file` which specifies the full path to a local image, so for example:

Open http://localhost:8000 on your browser

Upload any dog in the above categories
 poodle 
 pug 
 dachshund

And you will see the Image prediction and the confidence level in percentage

## License

Licensed under the Apache 2.0 license. See LICENSE file for details.
