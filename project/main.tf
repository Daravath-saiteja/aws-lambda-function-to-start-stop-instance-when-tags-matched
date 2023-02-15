provider "aws" {
  region = "eu-west-2"
}

resource "aws_instance" "example" {
  ami           = "ami-09ee0944866c73f62"
  instance_type = "t2.micro"
  

  tags = {
    Name = "example-instance"
  }

}
