from dataclasses import field
from rest_framework import serializers
from givito.account.serializers import UserMinimalSerializer

from givito.service.models import Category, Project, ProjectRegistrant

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'description']

class ProjectBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ['deleted_at']
        # read_only_fields = ['owner', 'category']

class ProjectSerializer(ProjectBaseSerializer):
    owner = UserMinimalSerializer()
    category = CategorySerializer()
    placeholder = serializers.SerializerMethodField()
    
    def get_placeholder(self, obj):
        if(obj.placeholder == "" or obj.placeholder == None):
            return None
        else:
            return obj.placeholder.url

class ProjectMinimalSerializer(ProjectSerializer):
    class Meta:
        model = Project
        fields = ['title', 'uuid', 'owner']

class ProjectRegistrantBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjectRegistrant
        exclude = ['deleted_at']

class ProjectRegistrantSerializer(ProjectRegistrantBaseSerializer):
    owner = UserMinimalSerializer()
    project = ProjectMinimalSerializer()
    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        if(obj.project.registrant == None):
            return "UNASSIGNED"
        elif(obj.project.registrant == obj.uuid):
            return obj.project.status
        else:
            return "DENIED"